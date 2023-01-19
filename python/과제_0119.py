# 홀수
answer=[]
for _ in range(7):
    number=int(input())
    if number % 2 == 1 :
        answer.append(number)

if len(answer)==0:
    print(-1)
else:
    print(sum(answer), min(answer),sep="\n")

# 더하기
s=map(int,input().split(','))
print(sum(s))

# 학점계산
## 1)
score=input()
dic={}
t=0
for i in ['A','B','C','D','F']:
    if i == 'F':
        dic[i]=0.0
        continue
    tt=0
    for j in ['+','0','-']:
        dic[i+j]=round(4.3-t-(0.3)*tt,2)
        tt+=1
    t+=1
print(dic[score])

##2)
score=input()
dic={}
t=0
for i in ['A','B','C','D','F']:
    if i == 'F':
        dic[i]=0.0
    tt=0
    for j in ['+','0','-']:
        dic[i+j]=round(4.3-t-(0.3)*tt,2)
        tt+=1
    t+=1
    if score in dic:
        print(dic[score])
        break

# 다이얼
n=input()
answer=0
dic={2:['A','B','C'],3:['D','E','F'],4:['G','H','I'],5:['J','K','L'],6:['M','N','O'],7:['P','Q','R','S'],8:['T','U','V'],9:['W','X','Y','Z']}
for i in n:
    if i == 1:
        answer+=2
    elif i == 0 :
        answer+=11
    else:
        for idx,value in dic.items():
            if i in value:
                answer+=idx+1
print(answer)

# 숫자의 개수
answer=1
for _ in range(3):
    answer*=int(input())

for i in range(10):
    print(str(answer).count(str(i)),sep='\n')

# 회사에 있는 사람
n=int(input())
dic={}
for _ in range(n):
    name, active=input().split()
    if name not in dic:
        dic[name]=active
    else:
        dic.pop(name)
for word in sorted(dic.keys(),reverse=True):
    print(word)