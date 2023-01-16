#6. JSON 데이터 활용 - 영화 다중 정보 활용
import json

# 아래 코드 수정 금지
movies_json = open("data/movies.json", encoding="UTF8")
movies_list = json.load(movies_json)

# 이하 문제 해결을 위한 코드 작성
movie=[]
for i in range(len(movies_list)):
    star={}
    for content in ['id','title','vote_average','overview','poster_path','genre_ids']:
        star[content]=movies_list[i][content]
    movie.append(star)
print(json.dumps(movie, indent=2,ensure_ascii=False))