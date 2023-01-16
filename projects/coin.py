import requests
import pprint
URL = 'https://api.bithumb.com/public/ticker/ALL_KRW'
response=requests.get(URL)
print(response)
print(type(response))
print(dir(response)) # 모든 속성, 메서드 호출
data=response.json()
print(data.get('data').get('BTC').get('closing_price'))
print(data['data']['BTC']['closing_price'])