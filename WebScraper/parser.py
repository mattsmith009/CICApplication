import twitterScraper
import asyncio

if __name__ == "__main__":
   scraperRun = asyncio.run(twitterScraper.main())
   tweets = scraperRun[0] # A list of tweets containing the keyword we searched for
   links = scraperRun[1][:]

optimizedLinks = [] # A list of links retrieved from Twitter posts

for link in links:
    if len(link) != 0: 
        optimizedLinks.append(link)

print(optimizedLinks)

# NOTE t.co in any links is a shortened Twitter link, but that doesn't necesarily mean that it leads to another Twitter post.   



