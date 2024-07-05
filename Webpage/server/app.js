const express = require('express');
const app = express();
const messages = require('./messages');
const bodyParser = require('body-parser');

const { spawnSync } = require('child_process');
const { readFile } = require('fs/promises');
const { appendFile } = require('fs/promises');
const { join } = require('path');
const pests = [];
let currDate = "";
app.set('view engine', 'ejs');
// parses incoming request bodies. 
app.use(bodyParser.urlencoded({extended: false}));

app.use(express.static('public'));

// The args are a path to a file and a callback func with two args. 
// Tells server what to do when get request is made. 
app.get('/', (req, res) => {
    res.render('index', { message: messages.home, pests: pests, date: currDate});
});
app.get('/summaries', (req, res) => {
    res.send(messages.summaries);
});

app.post('/submit', (req, res) => {
    const pest = req.body.pest;
    if (!pest) {
        const err = new Error('Please enter a pest name!');
        return err
    }
    pests.push(pest)
    console.log(`Pest submitted: ${pest}`);
    res.redirect('/');
});

app.post('/date', (req, res) => {
    const date = req.body.date;
    if (!date) {
        const err = new Error('Please enter a date!');
        return err
    }
    currDate = date;
    console.log(`The date range submitted was ${currDate}`);
    res.redirect('/');
})


app.get("/grab", async (req, res, next) => {
    // both of these defined at beginning
    console.log(`Current list of pests: ${pests}`);
    console.log(`Current date range: ${currDate}`);

    // await appendFile(

    // )
    let currPest = pests[0];
    const pythonProcess = await spawnSync('python3', [
        'WebScraper/twitterScraper.py', 
        'main', 
        JSON.stringify({currPest, currDate}), 
        'Webpage/server/results.json'
    ]);
    const result = pythonProcess.stdout?.toString()?.trim();
    const error = pythonProcess.stderr?.toString()?.trim();

    const status = result === 'OK';

    if (status) {
        const buffer = await readFile('Webpage/server/results.json'); 
        const resultParsed = JSON.parse(buffer?.toString());
        res.send(resultParsed.toString());
    } else {
        console.log(error);
        res.send(JSON.stringify({status: 500, message: 'Server Error'}));
    };
});
    


// use is called every time a request is made to server. 
app.use((req, res) => {
    res.status(404).send(messages.notFound);
})

app.get('/pests', (req, res) => {
    res.send(pests.join(', ')); 
})
const port = 3000; 
// Starts server and makes it listen for requests on port 3000
app.listen(port, () =>{
    console.log(`Server is running at http://localhost:${port}`);
});

app.use((err, req, res, next) => {
    console.error(err.stack); 
    res.status(500).send("Something went wrong!");
});
