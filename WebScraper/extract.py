import spacy 
from twitScrape import searchByUser, searchByKeyword
# same for insta
# same for facebook

nlp = spacy.load("output/model-best")
# nlp = spacy.load("output/model-last")

### Fill in scraping info here
keywords = []
users = []
### Fill in scraping info here

keywordsDict = searchByKeyword(keywords)
usersDict = searchByUser(users)

def createDataDictionary(rawTweets: dict) -> dict:
    for key in rawTweets: 
        for sentence in rawTweets[key]:
            doc = nlp(sentence)
            entity_dict = {}
            entity_dict[doc] = {}
            for ent in doc.ents: 
                entity_dict[doc][ent.label_] = ent.text

    return entity_dict
    
