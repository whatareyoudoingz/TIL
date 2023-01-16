import sys
sys.stdin = open("input.txt", "r")

N,X=map(int,input().split())
A=list(map(int,input().split()))

for e in A:
    if e>=X:
        A.remove(int(e))
print(*A)

