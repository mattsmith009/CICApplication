from typing import List, Dict, Tuple
from tweety import Twitter
from tweety.filters import SearchFilters
from deep_translator import GoogleTranslator
import json
from datetime import datetime
from helpers import backADay
from dateutil import tz

from_zone = tz.tzutc()
to_zone = tz.tzlocal()
app = Twitter("session")

### Fill in login info here 
username = ""
password = ""
### Fill in login info here

app.sign_in(username, password)
# app.connect()
# print(app.user)

def searchByUser(usernames: list) -> Dict[str, List[Tuple[str]]]:
    """
    Searches the Twitter database for Tweets posted by any of the users within usernames up to one day ago. Returns a dictionary 
    where the keys are the users and the corresponding value of each key is a list of tuples where each tuple contains a tweet and the time
    it was posted by the user (Mexico time) in YYYY-MM-DD HR:MIN:SEC-TZ format.
    """
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

def searchByKeyword(keywords: list) -> Dict[str, List[Tuple[str]]]:
    """
    Searches the Twitter database for Tweets posted within the last day containing any of the words within keywords. Returns a dictionary 
    where the keys are the keywords and the corresponding value of each key is a list of tuples each containing a tweet (string) and the time it was 
    posted by the user (Mexico time) in YYYY-MM-DD HR:MIN:SEC-TZ format.
    """
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
    

def writeover_user(new_data: any, filename='WebScraper/twitterData.json') -> None:
    """
        Writes the data stored in new_data to WebScraper/twitterData.json, overriding the data that was stored in 
        that json file before. 
    """
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data = {}
        file_data["twitterScrapes"] = [new_data]
        print("done")
        file.seek(0)
        json.dump(file_data, file, indent = 4)

def writeover_keyword(new_data: any, filename='WebScraper/twitterKeywordData.json') -> None:
    """
        Writes the data stored in new_data to WebScraper/twitterData.json, overriding the data that was stored in that json file 
        before.
    """
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data = {}
        file_data["twitterScrapes"].extend([new_data])
        print("done")
        file.seek(0)
        json.dump(file_data, file, indent = 4)

def write_user(new_data: any, filename='WebScraper/twitterData.json') -> None:
    """
        Writes the data stored in new_data to WebScraper/twitterData.json, adding onto 
        the data that was in that json file before. 
    """
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data = {}
        file_data["twitterScrapes"] = [new_data]
        print("done")
        file.seek(0)
        json.dump(file_data, file, indent = 4)

def write_keyword(new_data: any, filename='WebScraper/twitterKeywordData.json') -> None:
    """
        Writes the data stored in new_data to WebScraper/twitterData.json, adding onto the
        data that was stored in that json file before.
    """
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data = {}
        file_data["twitterScrapes"].extend([new_data])
        print("done")
        file.seek(0)
        json.dump(file_data, file, indent = 4)