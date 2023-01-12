import sys
sys.stdin = open("input.txt", "r")

#1
number=list(map(int,input().split()))
print(" ".join(str(i) for i in number))

#2
print(" ".join(input().split()))

#3
n=int(input())
for _ in range(n):
    m=int(input())
    for _ in range(m):
        print(int(input()))

#4
n=int(input())
for _ in range(n):
    m=int(input())
    for _ in range(m):
        print(" ".join(input().split()))

#5
n=int(input())
for _ in range(1,n+1):
    m=int(input())
    for _ in range(1,m+1):
        number=list(input().split())
        print(" ".join(i for i in number))

#6
n=int(input())
for _ in range(1,n+1):
    m=int(input())
    for _ in range(1,m+1):
        number=list(input().split())
        print(" ".join(number))

#7
n,m=list(map(int,input().split()))
for _ in range(1,n+1):
    for _ in range(1,m+1):
        print(int(input()))

#8
n,m=list(map(int,input().split()))
for _ in range(1,n+1):
    for _ in range(1,m+1):
        number=list(map(int,input().split()))
        print(" ".join(str(i) for i in number))

#9
n,m=list(map(int,input().split()))
for _ in range(1,n+1):
    for _ in range(1,m+1):
        number=list(map(int,input().split()))
        print(" ".join(str(i) for i in number))