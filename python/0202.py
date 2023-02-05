# 공
## 내 풀이
ball=[0,1,2,3]
for _ in range(int(input())):
    a,b=map(int,input().split())
    x,y=ball.index(a), ball.index(b)
    ball[x],ball[y]=ball[y],ball[x]
print(ball[1])

## 다른 사람 풀이 (백준 아이디 : dbwnwngus님)
ball=[0,1,2,3]
for _ in range(int(input())):
    a,b=map(int,input().split())
    ball[a],ball[b]=ball[b],ball[a]
print(ball[ball.index(1)])

# 콘테스트
w=sum(sorted([int(input()) for _ in range(10)],reverse=True)[:3])
k=sum(sorted([int(input()) for _ in range(10)],reverse=True)[:3])
print(w, k)

# 오르막길
T=int(input())
road=list(map(int,input().split()))
short, long=road[0], 0
i, ans=1, []
while True:
    if i==T:
        long=road[i-1] 
        ans.append(long-short)
        break
    if road[i]==road[i-1]: 
        short=road[i]
    if road[i]<road[i-1] :
        long=road[i-1] 
        ans.append(long-short )
        short=road[i] 
    i+=1
print(max(ans))
# 오르막길일때 최대값 갱신시키기
# 오르막길이었다가 내려막길일때
    # 최소값 교체, 최대값에서 교체 전 최소값 뺀 후 그 값이 저장되어 있는 최장 오르막길 길이보다 크다면  정답리스트에 저장
# 평지라면 최소값 리셋

## 다른 분 풀이 (최충현 님)
n = int(input())
height = list(map(int, input().split()))
temp = 0 # 임시저장 변수
a = [] # 오르막길 차이를 저장할 리스트

for i in range(1, n):
    if height[i] > height[i - 1]:
        temp += height[i] - height[i - 1] # (뒷길의 높이 - 앞길 높이)
        if i == n - 1: # 이전 높이보다 높으면서 마지막 위치라면(해당 조건문이 없으면 temp 변수 값이 a 리스트에 추가되지 못함)
            a.append(temp) # a 리스트에 temp 변수 값을 저장한다
    else:
        a.append(temp) # 이전 높이보다 크지 않을 때, temp 변수 값을 a 리스트에 추가하고
        temp = 0 # temp 변수를 초기화

print(max(a)) # a 리스트에 저장된 점수 중 가장 큰 값을 출력

## 강사님 풀이
N=int(input())
list_= list(map(int, input().split()))
# 단어 나누기
word =list(input())
li = []
for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        a,b,c= word[:i], word[i:j],word[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        li.append(''.join(a+b+c))
        li.sort()
print(li[0])

## 다른 분 풀이 (최충현 님)
word = input()
result = []
for i in range(len(word) - 2): # 길이가 1 이상인 3개의 단어로 구분해야함
    for j in range(i + 1, len(word) - 1):
        for k in range(j + 1, len(word)):
            new_word = word[:j][::-1] + word[j:k][::-1] + word[k:][::-1] # 모든 경우의 수를 뒤집은 후(역슬라이싱) 합친다
            result.append(new_word) # 합친 new_word 변수를 result 리스트에 추가

res_word = sorted(result) # sorted 함수를 통해 사전 순으로 정렬시킨 후에

print(res_word[0]) # 0번째 단어를 출력한다