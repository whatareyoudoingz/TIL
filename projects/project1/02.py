#2. 텍스트 파일 데이터 입출력

#파일 읽어서 수 카운트
f = open("data/fruits.txt", 'r')
total_sum=0
for line in f:
    total_sum+=1
f.close()

#텍스트파일에 저장하기
f1= open('02.txt','w')
f1.write(str(total_sum))
