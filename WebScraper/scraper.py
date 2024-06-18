import requests
from bs4 import BeautifulSoup

# this is an easy example...There are no cookies or login pages blocking the text. 
URL = "https://link.springer.com/article/10.1007/s10530-011-9937-6" # Make this into a user input eventually
page = requests.get(URL)
soup = BeautifulSoup(page.text, 'html.parser')
body_content = soup.find("div", class_ = "c-article-body")
body_text = body_content.find("div", class_ = "main-content").text

# print(body_text)

# slightly more copmlicated example

URL2 = "https://www.sciencedirect.com/science/article/pii/S1110982323000662"
page2 = requests.get(URL2)
soup2 = BeautifulSoup(page2.text, 'html.parser')

print(soup2.text)