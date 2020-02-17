import bs4 as bs
import requests

sorce=requests.get('http://quotes.toscrape.com/').text
soup=bs.BeautifulSoup(sorce,'lxml')
match=soup.find_all('div')
print(sorce)

