import spacy 
from twitScrape import searchByKeyword, searchByUser
# same for insta
# same for facebook

nlp = spacy.load("output/model-best")
# nlp = spacy.load("output/model-last")

test_sentences = [ "alphavirus has created 25 infections in the past two years in Alabama."]

doc = nlp("".join(test_sentences))

for ent in doc.ents: 
    print(ent.text, ent.label_)
    
keywords = []
users = []