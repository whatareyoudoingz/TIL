import sys
sys.stdin = open("input_1.txt", "r")

# 딕셔너리 생성
n=int(input())
dic=dict()
for i in range(n):
    for j in range(n):
        dic[i,j]=f"{i+1}/{j+1}"
print(dic)

t=0
i,j=0.0
for i in range(len(x))::
step=[(i,j+1),(i+1,j-1),(i+1,j),(i-1,j+1)]

i,j=i,j+1
i,j=i+1,j-1
i,j=i+1,j
i,j=i-1,j+1
