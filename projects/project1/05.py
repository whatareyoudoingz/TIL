#5. JSON 데이터 활용 - 영화 단일 정보
import json

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

# 이하 문제 해결을 위한 코드 작성
#필요한 정보만 모은 딕셔너리 생성 
star={}
for content in ['id','title','vote_average','overview','genre_ids']:
    star[content]=movie[content]

print(json.dumps(print_movie, indent=2,ensure_ascii=False))