import requests
from bs4 import BeautifulSoup

browser = requests.get("https://www.inshorts.com/en/read")
# print(browser.text)
soup = BeautifulSoup(browser.content,'lxml')
news_cards = soup.find_all('div',{"class":"news-card"})
for i in range(len(news_cards)):
    print(news_cards[i].find('div',{'class':"news-card-title"}).find('a').getText())
    print(news_cards[i].find('div',{'class':"news-card-content"}).find('div',{"itemprop":"articleBody"}).getText())
    try:
        print(news_cards[i].find('div',{'class':"read-more"}).find('a',{"class":"source"})['href'])
        print(news_cards[i].find('div',{'class':"read-more"}).find('a',{"class":"source"}).getText())
    except:
        print('Null')
