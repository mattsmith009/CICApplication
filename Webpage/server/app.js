const express = require('express');
const app = express();
const messages = require('./messages');
const bodyParser = require('body-parser');
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
app.get('/Summaries', (req, res) => {
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
