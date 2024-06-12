import requests

URL = "https://www.nature.com/articles/s41598-024-52861-3"
page = requests.get(URL)
print(page.text)