import sys
sys.stdin = open("input_1.txt", "r")

T=int(input())
room=[list(input()) for _ in range(T)]
total=0

# 가로부터 체크
room1=room
for i in range(T):
    for j in range(T):
        if room1[i][j]=='.' : # 빈방이면
            if j==0 or room1[i-1][j]=='X': # 처음이면 계속
                a=1
            else: #아니면 길이 체크 (변수 a) 후 0으로 공실 만들어주기
                a+=1
                room1[i][j]=0
        else: # 빈방이 아니면
            if a > 1: # 길이가 1이 아니면 카운트
                total+=1
            else: # 길이가 1이면 카운트 제외
                a=0
print(total)

# 세로부터 체크
room2=room
for j in range(T):
    for i in range(T):
        if room2[i][j]=='.' : # 빈방이면
            if i==0: # 처음이면 계속
                a=1
                continue
            else: #아니면 길이 체크 (변수 a) 후 0으로 공실 만들어주기
                a+=1
                room2[i][j]=0
        else: # 빈방이 아니면
            if a > 1: # 길이가 1이 아니면 카운트
                total+=1
            else: # 길이가 1이면 카운트 제외
                a=0
print(total)

