# 별 찍기 -4
n=int(input())
for i in range(n):
    print(" "*i+"*"*(n-i))

# 대표값
## 이차원 리스트를 이용하여 구현
number=[[0]*10 for _ in range(2)]
result=0
for i in range(10):
    n=int(input())
    result+=n
    if n not in number[0]:
        number[0][i]=n
        number[1][number[0].index(n)]=1
    else:
        number[1][number[0].index(n)]+=1
print(result//10, number[0][number[1].index(max(number[1]))],sep='\n')

## 다른 분 풀이 ( 한선진 님)
https://docs.python.org/ko/dev/library/statistics.html
import statistics
a=[]
for i in range(10):
    num=int(input())
    a.append(num)
print(sum(a)//10)
print(statistics.mode(a))

# 세로 읽기
string=[]
for _ in range(5):
    n=input()
    string.append(list(n)+[-1]*(15-len(n)))

for j in range(15):
    for i in range(5):
        if string[i][j] != -1 :
            print(string[i][j],end="")
        else:
            continue

## 다른 분 풀이 (박지현 님)
string_list = [list(input()) for _ in range(5)]

for i in range(15):
    for j in range(5):
        if i < len(string_list[j]):
            print(string_list[j][i], end='')

# 박스
for _ in range(int(input())):
    result=0
    m,n=map(int,input().split())
    box=[list(input().split()) for _ in range(m)]
    for j in range(n):
        if box[m-1][j]=='1': #맨 밑에 상자가 있을 때
            for i in range(m-1):#처음부터 맨 밑 전까지 빈칸 세기 
                if box[i][j]=='1':#박스가 있다면 그 다음부터 끝까지 빈칸 세기
                    for k in range(i+1,m-1):
                        if box[k][j]=='0': 
                            result+=1
                if box[i][j]=='0': 
                    continue
        else: #맨 밑에 상자가 없을 때
            for i in range(m):#처음부터 맨 밑까지 빈칸 세기
                if box[i][j]=='1':#박스가 있다면 그 다음부터 끝까지 빈칸 세기
                    for k in range(i+1,m):
                        if box[k][j]=='0': 
                            result+=1
                if box[i][j]=='0': 
                    continue
    print(result)

## 함수화
def box_checker(a):
    global i,j,result
    for i in range(a):#처음부터 빈칸 세기 (맨 위 상자)
        if box[i][j]=='1': #박스가 있다면 그 다음부터 끝까지 빈칸 세기
            for k in range(i+1,a):
                if box[k][j]=='0': 
                    result+=1
        if box[i][j]=='0': 
            continue

for _ in range(int(input())):
    result=0
    m,n=map(int,input().split())
    box=[list(input().split()) for _ in range(m)]
    for j in range(n):
        if box[m-1][j]=='1': #맨 밑에 상자가 있을 때
            box_checker(m-1)
        else: #맨 밑에 상자가 없을 때
            box_checker(m)
    print(result)

## 강사님 풀이
for _ in range(int(input())):
    m, n = map(int, input().split())
    box = [input().split() for _ in range(m)]
    move_dis=0
    for x in range(n):
        for y in reversed(range(m)):
            if grid[y][x]==1:
                while True:
                    if y+1 ==m:
                        break
                    if grid[y+1][x]==1:
                        break

                    grid[y][x]=0
                    grid[y+1][x]=0
                    move_dis+=1
                    y+=1
print(move_dis)

## 다른 분 풀이 (최충현 님)
for _ in range(int(input())):
    m, n = map(int, input().split())
    box = [input().split() for _ in range(m)]
    move_box = 0
    for j in range(n):
        cnt = 0
        for i in range(m -1, -1, -1): # (0, 0) 위치부터 탐색
            if box[i][j] == '1':
                move_box += cnt # '1' 를 만났을 때, 변수 cnt 값 더하여 대입
            else:
                cnt += 1 # '0'일 때 cnt에 1씩 더하여 대입
    print(move_box)

# 누울 자리를 찾아라
T=int(input())
room=[list(input()) for _ in range(T)]
width,length=0,0
# 가로부터 체크
for i in range(T):
    a=0 #연속 공실 카운트
    for j in range(T):
        #빈방이고 길이 체크 (변수 a) 후 0으로 공실 만들어주기
        if room[i][j]=='.' :  
                a+=1
        elif room[i][j]=='X': # 빈방이 아니면
            if a > 1: # 길이가 1이 아니면 카운트
                width+=1
            a=0
        if j==T-1:
            if a > 1: # 길이가 1이 아니면 카운트
                width+=1

# 세로부터 체크
for j in range(T):
    a=0 #연속 공실 카운트
    for i in range(T):
        #빈방이고 길이 체크 (변수 a) 후 0으로 공실 만들어주기
        if room[i][j]=='.' :  
                a+=1
                room[i][j]=0
        elif room[i][j]=='X': # 빈방이 아니면
            if a > 1: # 길이가 1이 아니면 카운트
                length+=1
            a=0
        if i==T-1:
            if a > 1: # 길이가 1이 아니면 카운트
                length+=1
print(width, length)

## 다른 분 풀이 (전성재 님)
N = int(input())
matrix = [list(map(str, input().strip())) for _ in range(N)]

row = 0
column = 0

for y in range(N):
    cnt = 0
    for x in range(N):
        if matrix[y][x] == '.':
            cnt += 1

        elif matrix[y][x] == 'X':
            if cnt >= 2:
                row += 1
            cnt = 0
    if cnt >= 2:
        row += 1
    cnt = 0

for x in range(N):
    cnt = 0
    for y in range(N):
        if matrix[y][x] == '.':
            cnt += 1

        elif matrix[y][x] == 'X':
            if cnt >= 2:
                column += 1
            cnt = 0
    if cnt >= 2:
        column += 1
        column += 1
    cnt = 0

print(row, column)