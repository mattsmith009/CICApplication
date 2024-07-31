# CICApplication

## **Instructions to Scrape**

Twitter - 
Scraping by Keyword: The list of keywords to scrape is stored in the 'keywords' list. When you want to scrape a word, add it to that
list. The scraper will scrape all the words within that list and return Tweets from up to one day ago. 

Scraping by User: The list of accounts to scrape from is stored in the 'users' list. If there is a Twitter account that you would 
like to scrape from, add it to this users list. The scraper will scrape tweets from all users from up to a day ago. 

Facebook - 

Instagram - 

## **Using the Tool**

Inputing data - 

Running the scrapers - 

Gathering results - 

## **Training Data**

Disease data - All diseases of importance are in the file named 'training_examples.py'. Training data for diseases has all been based on this data. Some of the data has been obtained through Twitter scraping, while others have been generated through tools such as ChatGPT. If you would like to create more training data, those are the methods I would recommend.

Numerical data - All numerical data has been obtained through tools such as TWitter scraping and ChatGPT. It provides an alright amount of diversity, with Tweets providing the best. In the case that you would like to provide more training data, I believe Twitter would provide the best results. 

Location data - Location data has been obtained through internet searches, ChatGPT, and Twitter. Twitter again provides the most realistic data, but all sources are a good source of data. 

## **Examples**

## **Error Handling**

Scraping social media can be elusive because of restrictions and rate limits placed on these apps by their executives in order to restrict the flow of information. For these scrapers, there are some weird errors that you will have to handle. Below I detail how I dealt with them throughout the process of scraping. 

### Twitter 

"tweety.exceptions.RateLimitReached: [88] Rate limit exceeded" This means that you have reached the allowed scraping limits by Twitter. As of July 2024, the rate limit is 900 requests per 15 minutes. If you encounter this, you just need to wait 15 minutes until scraping again. 
