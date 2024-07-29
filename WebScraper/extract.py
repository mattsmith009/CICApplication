import spacy 
from twitScrape import searchByKeyword, searchByUser
# same for insta
# same for facebook

nlp = spacy.load("output/model-best")
# nlp = spacy.load("output/model-last")

keywords = []
users = []



