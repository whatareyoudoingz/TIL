# 이상한 곱셈
import sys
a,b=map(list,sys.stdin.readline().split())
print(sum(map(int,a))*sum(map(int,b)))

# 별 찍기 -1
for i in range(int(input())):
	print("*"*(i+1))
	
# 구구단
n=int(input())
for i in range(1,10):
    print(f"{n} * {i} = {n*i}" )

# 나는 요리사다
score={}
for i in range(5):
    score[i]=sum(map(int,input().split()))

##1
for x,y in score.items():
    if y == max(score.values()):
        print(x+1,y)

##2
print(b.index(max(score.values())+1, max(score.values())))

# 직사각형 네개의 합집합의 면적 구하기
space=[[0]*101 for _ in range(101)]
for _ in range(4):
    x1,y1,x2,y2=map(int,input().split())
    for x in range(x1,x2):
        for y in range(y1,y2):
            space[x][y]=1

result=0
for i in range(len(space)):
    for j in range(len(space)):
        if space[i][j]==1:
            result+=1
print(result)


## 다른 분 풀이 (최충현 님)
matrix = []

for _ in range(4):
    num = list(map(int, input().split()))
    for i in range(num[0], num[2]):
        for j in range(num[1], num[3]):
            matrix.append((i, j))

print(len(set(matrix)))