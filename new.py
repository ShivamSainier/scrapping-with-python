import bs4 as bs
import requests
http='https://coreyms.com/'
req=requests.get(http).text
soup=bs.BeautifulSoup(req,'lxml')
#print all articles
article=soup.find_all('article')
print(article)


#find=soup.find('iframe',class_="youtube-player")['src']
#l=find.split('/')[4]
#l=l.split('?')[0]
#print(l)
