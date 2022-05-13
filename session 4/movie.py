import urllib
import urllib.request
import json
from urllib import parse
from bs4 import BeautifulSoup
import requests
client_id = "" 
client_key = "" 
#movies=input("영화를 입력해주세요:")
encText = urllib.parse.quote("기생충")
url = "https://openapi.naver.com/v1/search/movie.json?query=" + encText # json 결과


request = urllib.request.Request(url)
header={}
header["X-Naver-Client-Id"]=client_id
header["X-Naver-Client-Secret"]=client_key

response= requests.get(url,headers=header)

#soup=BeautifulSoup(response.text,'html.parser')
#print(soup.find('b')["title"])

data=json.loads(response.text)
item=data["items"]
movie_title = item[0]['title']
movie_link = item[0]['link']
movie_director= item[0]['director']
movie_title_removedB = item[0]['title'].replace('</b>','').strip('<b>')
movie_director_one= item[0]['director'].split('|')[0]
print(movie_director_one)