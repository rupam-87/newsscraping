import bs4
from bs4 import BeautifulSoup as soup
import requests

news_url="https://news.google.com/news/rss"
Client=requests.get(news_url)
soup_page=soup(Client.text,"xml")
soup=soup(Client.text,"html.parser")
news_list=soup_page.findAll("item")
for news in news_list:
  print(news.title.text)
  print(news.link.text)
  print(news.pubDate.text)
