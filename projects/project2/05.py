import requests
from pprint import pprint


def recommendation(title):
    pass
    # 여기에 코드를 작성합니다.
    BASE_URL='https://api.themoviedb.org/3'
    path='/search/movie'
    params={
        'api_key':API_KEY,
        'query':title,
        'language':'ko-KR',
        'region':'KR'
        }

    response=requests.get(BASE_URL+path, params=params).json()
    answer=response['results']
    try: 
        answer=answer[0]['id']
        path1=f'/movie/{answer}/recommendations'
        params1={
            'api_key':API_KEY,
            'language':'ko-KR',
            'region':'KR'
            }

        response1=requests.get(BASE_URL+path1, params=params1).json()
        answer1=response1['results'] 
        try: 
            total_answer=[]
            for j in range(len(answer1)):
                total_answer.append(answer1[j]['title'])
        except:
            total_answer=[]  
        return total_answer
    except:
        answer=None

    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
