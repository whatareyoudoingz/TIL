#1110 더하기 사이클
n=input()
if len(n)==1:
    n='0'+n
a,b=int(n[0]),int(n[1])
answer, string, i =a+b, 0, 0  #첫 숫자 a+b, 문자열ab, 카운트
while string!=n: #숫자가 입력값과 다를때 반복
    a=b #6
    b=int(str(answer)[-1]) #8
    string=str(a)+str(b) #68 #문자열 ab
    answer=a+int(string[-1]) #14  #숫자 a+b
    i+=1
print(i)

#10952 A+B-5    
while True:
    a,b=map(int,input().split())
    if a==0 and b==0:
        break
    else:
        print(a+b)

# 네번째 점
lis_x,lis_y=[],[]

for _ in range(3):
    a,b=input().split()
    lis_x.append(a)
    lis_y.append(b)

for k in lis_x:
    if lis_x.count(k)<2:
        x=k
for q in lis_y:
    if lis_y.count(q)<2:
        y=q
print(x,y)

# 10824 네 수
number=list(input().split())
number1=number[0]+number[1]
number2=number[2]+number[3]
print(int(number1)+int(number2))

# 9085 더하기
for _ in range(int(input())):
    n=int(input())
    number=list(map(int,input().split()))
    print(sum(number))