# 4. 텍스트 파일 데이터 활용 - 단어 등장 횟수

#파일 읽어서 카운트 딕셔너리만들기
f = open("data/fruits.txt", 'r')
dic={}
for line in f:
    line=line.strip()
    if line not in dic:
        dic[line]=1
    else:
        dic[line]+=1

f.close()

#텍스트파일에 저장하기
f1= open('04.txt','w')
for name,tot in dic.items():
    f1.write(f"{name} {tot} \n")
