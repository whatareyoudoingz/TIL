import json

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

genres_json = open("data/genres.json", encoding="UTF8")
genres_list = json.load(genres_json)

# 이하 문제 해결을 위한 코드 작성 
answer=[]
for x in movie['genre_ids']: #영화 장르 아이디
    for y in genres_list: #영화 장르 
        if y['id']==x: #영화 장르의 아이디가 일치한다면
            answer.append(y['name']) #영화 장르 이름 추가
print(answer)