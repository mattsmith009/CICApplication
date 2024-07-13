import twitterScraper
import asyncio
from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import numpy as np
from scipy.special import softmax

# Need to get the user inputs to the HTML file and then use it as an argument in the main function.

if __name__ == "__main__":
   scraperRun = asyncio.run(twitterScraper.scrape())
   tweets = scraperRun[0] # A list of tweets containing the keyword we searched for
   links = scraperRun[1][:]

optimizedLinks = [] # A list of links retrieved from Twitter posts

for link in links:
    if len(link) != 0: 
        optimizedLinks.append(link)

print(optimizedLinks)
print(tweets)
# NOTE t.co in any links is a shortened Twitter link, but that doesn't necesarily mean that it leads to another Twitter post.  

# Preprocess text (username and link placeholders)
def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)
MODEL = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
config = AutoConfig.from_pretrained(MODEL)
# # PT
model = AutoModelForSequenceClassification.from_pretrained(MODEL)
#model.save_pretrained(MODEL)

# for key in tweets: 
#     text = tweets[key]
#     text = preprocess(text)
#     encoded_input = tokenizer(text, return_tensors='pt')
#     output = model(**encoded_input)
#     scores = output[0][0].detach().numpy()
#     scores = softmax(scores)
#     # Print labels and scores
#     ranking = np.argsort(scores)
#     ranking = ranking[::-1]
#     for i in range(scores.shape[0]):
#         l = config.id2label[ranking[i]]
#         s = scores[ranking[i]]
#     #     print(f"{i+1}) {l} {np.round(float(s), 4)}")
#     # print('\n')
