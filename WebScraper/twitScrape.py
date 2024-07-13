from tweety import Twitter
from deep_translator import GoogleTranslator
import json
from datetime import datetime

username = "spazmattie"
password = "06M03s04"

app = Twitter("session")
app.sign_in(username, password)
# print(app.user)

usernames = ["Tu_IMSS", "Agricultura_mex"]
tweetsDict = {}

for user in usernames: 
    tweetsDict[user] = []
    tweets = app.get_tweets(username=user)
    for tweet in tweets: 
        # tweetsDict[user].append([GoogleTranslator(source='es', target='en').translate(tweet.text), str(tweet.date)])
        tweetsDict[user].append([tweet.text, str(tweet.date)]) # times are in UTC which is 6 hours ahead of Mexico.

for key in tweetsDict: 
    for tweet in tweetsDict[key]:
        print(tweet)
        print('\n')

# turn it into JSON data. 
def write_json(new_data, filename='WebScraper/twitterData.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data = {}
        file_data["twitterScrapes"] = [new_data]
        file_data["datetime"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

write_json(tweetsDict)