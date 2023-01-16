#3. 텍스트 파일 데이터 활용 - 특정 단어 추출

#파일 읽어서 리스트와 수만들기
f = open("data/fruits.txt", 'r')
dic=[]
total_sum=0

for line in f:
    line=line.strip()
    if "berry" == line[-5:]:
        if line not in dic:
            total_sum+=1
            dic.append(line)
f.close()

#텍스트파일에 저장하기
f1= open('03.txt','w')
f1.write(str(total_sum)+"\n")
for name in dic:
    f1.write(name+"\n")
