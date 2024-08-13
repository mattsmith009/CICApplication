import spacy 
import json 
from twitScrape import searchByUser, searchByKeyword
# same for insta
# same for facebook

nlp = spacy.load("output/model-best")
# nlp = spacy.load("output/model-last")

### Fill in scraping info here
keywords = ['']
users = ['']
### Fill in scraping info here

keywordsDict = searchByKeyword(keywords)
usersDict = searchByUser(users)

def createDataDictionary(rawTweets: dict) -> dict:
    """
    Given a dictionary in which keywords are matched to a list of lists where each inside list contains a tweet along with its timestamp.
    """
    entity_dict = {}
    for key in rawTweets: 
        for sentence, timestamp in rawTweets[key]:
            doc = nlp(sentence)
            entity_dict[doc] = {}
            for ent in doc.ents: 
                entity_dict[doc][ent.label_] = ent.text
            
            entity_dict[doc]['TIMESTAMP'] = timestamp

    return entity_dict

def write_extracted(data: dict, filename = 'WebScraper/extracted.json', writeover = False) -> None: 
    with open(filename,'r+') as file:
        file_data = json.load(file)
        if writeover: 
            file_data = {}
            for key in data:
                file_data[str(key)] = data[key]   

        if not writeover: 
            for key in data: 
                if key not in file_data: 
                    file_data[str(key)] = data[key]
        print("done")
        file.seek(0)
        json.dump(file_data, file, indent = 4)

currData = createDataDictionary(keywordsDict)
write_extracted(currData, writeover = True)
