# 평균 점수
total_score=0
for _ in range(5):
    score=int(input())
    if score >= 40:
        total_score+=score
    else:
        total_score+=40
print(total_score//5)

# X보다 작은 수
##1
n ,x=map(int,input().split())
a=list(map(int,input().split()))
answer=[]
for number in a:
    if number < x:
        answer.append(number)
    else:
        continue
print(" ".join(str(i) for i in answer))

##2 숏코딩
n, v=map(int,input().split())
lis=list(map(int,input().split()))

print(" ".join(str(i) for i in lis if i < v))

# 주사위 세개
a,b,c=list(map(int,input().split()))

n1=a==b
n2=a==c
n3=b==c
total=n1+n2+n3
if total == 3:
    print(10000+a*1000)
elif total == 1:
	if a==b or a==c:
        print(1000+a*100)
	else:
        print(1000+b*100)
elif total == 0:
	print(max(a,b,c)*100)

# 0 = not cute / 1 = cute
## 1
n=int(input())

total=0
for _ in range(n):
    ans=int(input())
    total+=ans
if total > (n//2):
    print("Junhee is cute!" )
else:
    print("Junhee is not cute!")

##2 숏코딩
n=int(input())
total=0
for _ in range(n):
    ans=int(input())
    total+=ans
print("Junhee is cute!" if total > (n//2) else "Junhee is not cute!")

# 점수계산
## 아이디어 : 입력 리스트를 점수 저장소로 사용하자!
n=int(input())
array=list(map(int,input().split()))

for i in range(n):
    if i == 0 : #맨 처음에는 그대로 둬라
        continue
    if array[i] == 1: # 1이라면
        if array[i-1] != 0 : # 그 전 문제를 맞췄다면 # 연속으로 맞췄을 경우
            array[i] = array[i-1]+1 #연속적으로 1을 더해줘라
print(sum(array)) #합을 출력해라
