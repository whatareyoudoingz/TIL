import requests
from pprint import pprint


def credits(title):
    pass
    # 여기에 코드를 작성합니다.
    BASE_URL='https://api.themoviedb.org/3'
    path='/search/movie'
    params={
        'api_key':'d6c37aea2540250bc851eccf03e94787',
        'query':title,
        'language':'ko-KR',
        'region':'KR'
        }

    response=requests.get(BASE_URL+path, params=params).json()
    answer=response['results']
    try: 
        answer=answer[0]['id']
        path1=f'/movie/{answer}/credits'
        params1={
            'api_key':'d6c37aea2540250bc851eccf03e94787',
            'language':'ko-KR',
            'region':'KR'
            }

        response1=requests.get(BASE_URL+path1, params=params1).json()
        answer1=response1['cast'] 
        answer2=response1['crew']
        total_answer={'cast':[],'crew':[]}
        for j in range(len(answer1)):
            if  answer1[j]['cast_id'] < 10:
                total_answer['cast'].append(answer1[j]['name'])
        for q in range(len(answer2)):
            if answer2[q]['department']=="Directing":
                total_answer['crew'].append(answer2[q]['name'])
        return total_answer
    except:
        answer=None


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록 반환
    영화 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
