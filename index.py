import requests
from bs4 import BeautifulSoup

result = requests.get("https://duckduckgo.com/?q=%22gmail.com%22+%22yahoo.com%22+%22mail.com%22+site%3Ainstagram.com&t=h_&ia=web")
soup = BeautifulSoup(result.content, "html.parser")
print(soup)
# # print(soup.find_all('a'))
# for item in soup.find_all('a'):
#     print(item.text)
