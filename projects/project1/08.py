import json

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

genres_json = open("data/genres.json", encoding="UTF8")
genres_list = json.load(genres_json)

# 이하 문제 해결을 위한 코드 작성
answer=[]
for x in movie['genre_ids']:
    for y in genres_list:
        if y['id']==x:
            answer.append(y['name'])

star={}
for content in ['id','title','vote_average','overview','genre_ids']:
    if content == 'genre_ids': #장르 아이디는 장르 이름으로 대체
        star[content]=answer
    else:
        star[content]=movie[content]


##이쁘게 출력 
import pprint
pprint.pprint(star)