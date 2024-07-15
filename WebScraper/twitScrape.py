from tweety import Twitter
from tweety.filters import SearchFilters
from deep_translator import GoogleTranslator
import json
from datetime import datetime, timezone
from helpers import backADay
from dateutil import tz

username = "spazmattie"
password = "06M03s04"
from_zone = tz.tzutc()
to_zone = tz.tzlocal()
app = Twitter("session")
app.sign_in(username, password)
# print(app.user)
usernames = ["Tu_IMSS", "Agricultura_mex"]
keywords = ["alphavirus", "japanese encephalitis"]

def searchByUser(usernames: list):
    userTweetsDict = {}
    cutoff = backADay(datetime.now()).replace(tzinfo=to_zone)
    for user in usernames: 
        userTweetsDict[user] = []
        tweets = app.get_tweets(username=user, pages=1)

        for tweet in tweets: 
            tweetDate = tweet.date.replace(tzinfo=to_zone)
            if tweetDate < cutoff: 
                break
            else: 
                # userTweetsDict[user].append([GoogleTranslator(source='es', target='en').translate(tweet.text), str(tweetDate)])
                userTweetsDict[user].append([tweet.text, str(tweetDate)]) 

    return userTweetsDict

def searchByKeyword(keywords: list):
    keywordTweetsDict = {}
    cutoff = backADay(datetime.now()).replace(tzinfo=to_zone)
    for keyword in keywords: 
        keywordTweetsDict[keyword] = []
        tweets = app.search(keyword, filter_=SearchFilters.Latest())
        for tweet in tweets:
            tweetDate = tweet.date.replace(tzinfo=to_zone)
            if tweetDate < cutoff: 
                break 
            else:
                # keywordTweetsDict[keyword].append([GoogleTranslator(source='es', target='en').translate(tweet.text), str(tweetDate)])
                keywordTweetsDict[keyword].append([tweet.text, str(tweetDate)]) 

    return keywordTweetsDict
    
# turn it into JSON data. 
def write_user_json(new_data, filename='WebScraper/twitterData.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data = {}
        file_data["twitterScrapes"] = [new_data]
        print("done")
        file.seek(0)
        json.dump(file_data, file, indent = 4)

def write_keyword_json(new_data, filename='WebScraper/twitterKeywordData.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data = {}
        file_data["twitterScrapes"] = [new_data]
        print("done")
        file.seek(0)
        json.dump(file_data, file, indent = 4)

write_user_json(searchByUser(usernames))
write_keyword_json(searchByKeyword(keywords))