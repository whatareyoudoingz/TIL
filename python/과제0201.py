# 오븐 시계
a,b=list(map(int,input().split()))
c=int(input())

top=c//60
if top <=0:
	b+=c
else:
    a+=top
    bot=60*top
    b+=c-bot

if b >= 60:
    a+=b//60
    b%=60

if a >= 24:
    a-=24
print(a,b)

## 다른 분 풀이 (전성재 님)
a, b = map(int, input().split())
c = int(input())
b += c
if b >= 60:
    a += (b // 60)
    b %= 60
    if a >= 24:
        a %= 24
print(a, b)

## 다른 분 풀이 2 (한선진 님)
h, m = list(map(int,input().split()))
a = int(input())

m += a # 분 더하기 
h += m //60 # 시에 분 더해서 60 나눈 몫 

m %= 60 # 60분으로 나눈 나머지
h %= 24 # 24시로 나눈 나머지 
print(h,m) 

# 블랙잭
n,m=map(int,input().split())
number=list(input().split())

max=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            tot=int(number[i])+int(number[j])+int(number[k])
            if max <  tot and tot <= m:
                max=tot
print(max)

# 점수 집계
for _ in range(int(input())):
    number=sorted(list(map(int,input().split())),reverse=True)[1:-1]
    n=number[0]-number[-1]
    if n >=4 : 
        print("KIN")
    else:
        print(sum(number))

## 숏코딩
for _ in range(int(input())):
    number=sorted(list(map(int,input().split())),reverse=True)[1:-1]
    print("KIN" if number[0]-number[-1] >=4 else sum(number))

# 가장 큰 금민수
T=int(input())
top=0
for i in range(T+1):
    call=set(str(i))-set(('4','7'))
    if len(call)==0 and top <  i <= T+1:
        top=i
print(top)

## 다른 분 풀이 (최충현 님)
n = int(input())
for i in range(n, -1, -1):
    if all([(s == '4' or s == '7') for s in str(i)]):
        print(i)
        break

# 영화 감독 숌
T=int(input())
cnt, i=0, 666
while True:
    if '666' in str(i):
        cnt+=1
    if cnt == T:
        print(i)
        break
    i+=1