# beautifl soup fetches the data directly fro online website
from bs4 import BeautifulSoup
# file=open("Hello.html")
# soup=BeautifulSoup(file.read(),"html.parser")#parse means to convert
# soup.find()
# soup.title
# print(soup.title)
from urllib import request
# resp=request.urlopen("https://www.google.com/")
resp=request.urlretrieve("https://www.google.com/","google.html")
file=open("google.html")
soup=BeautifulSoup(file.read(),"html.parser")
# print(soup.title)
print(soup.a)#anchor tag
# print(soup.find_all("a"))# (a) denotes anchor tag (p) denotes paragraph
l=soup.find_all('a')
# for i in soup.find_all("span"):
#     print(i) print all the span tags in list one by one
# for i in l:
#     if i.has.attr("href"):
#         print(item["href"])






