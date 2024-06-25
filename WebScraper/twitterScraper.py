import asyncio
from twscrape import API, gather
from twscrape.logger import set_log_level
import re 

async def main(): 
    api = API() 
    await api.pool.add_account("spazmattie", "06M03s04", "mattboi2004@icloud.com", "Matt$&Sam2")
    await api.pool.login_all()

    await gather(api.search("elon musk", limit=20))

    tweet_id = 20
    await api.tweet_details(tweet_id)  # Tweet
    await gather(api.retweeters(tweet_id, limit=20))  # list[User]
    await gather(api.favoriters(tweet_id, limit=20))

    await gather(api.tweet_replies(tweet_id, limit=20))

    # list info
    list_id = 123456789
    await gather(api.list_timeline(list_id))

    listOfTweets = {}
    # NOTE 1: gather is a helper function to receive all data as list, FOR can be used as well:
    async for tweet in api.search("alphavirus, since:2024-06-19"):
        # print(tweet.id, tweet.user.username, tweet.rawContent)  # tweet is `Tweet` object
        listOfTweets[tweet.id] = tweet.rawContent
    
    linkRegex =  r"https?://(?:www\\.)?[a-zA-Z0-9./]+"
    links = []
    for key in listOfTweets: 
        print(str(key) + ": " + listOfTweets[key])
        print("\n")
        links.append(re.findall(linkRegex, listOfTweets[key]))
        # need to detect links in a post and navigate to that post to determine if it is important or not. 
        # use the regex (or find a better one)
    
    # print(links)
    # change log level, default info
    set_log_level("DEBUG")
    return listOfTweets, links
