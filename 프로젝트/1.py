import requests

#실습예시
BASE_URL='https://api.themoviedb.org/3'
path='/movie/popular'
params={
    'api_key':'d6c37aea2540250bc851eccf03e94787',
    'language':'ko-KR',
    'region':'KR'
}

response=requests.get(BASE_URL+path, params=params).json()
print(response)
print(response.get('result')[0])