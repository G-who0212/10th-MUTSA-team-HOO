import secrets
import requests
import json

headers = {
    'X-Naver-Client-Id': secrets.Naver_client_id,
    'X-Naver-Client-Secret': secrets.Naver_client_secret
}

name = input("검색할 영화를 입력해주세요 : ")

url = f"https://openapi.naver.com/v1/search/movie.json?query={name}"

response = requests.get(url, headers=headers)

data = json.loads(response.text)

title = data['items'][0]['title'].replace('</b>','').strip('<b>')
link = data['items'][0]['link']
director=data['items'][0]['director'].split('|')[0]

print(title)
print(link)
print(director)