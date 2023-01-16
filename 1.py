import sys
sys.stdin = open("input.txt", "r")

a=int(input())
for _ in range(a):
    b,c=map(int,input().split(','))
    print(b+c)