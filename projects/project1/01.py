#1. 텍스트 파일 데이터입력

#파일 생성 & 쓰기 
## https://wikidocs.net/26
## https://docs.python.org/ko/3/tutorial/inputoutput.html#reading-and-writing-files
f= open('01.txt','w')

for i in range(6):
    if i ==0:
        f.write("Hello, Python! \n")
    else:
        data=f"{i}일차 파이썬 공부 중 \n"
        f.write(data)
f.close()

#파일 읽기
f = open("01.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()