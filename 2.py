import sys
sys.stdin = open('input.txt','r')

n=int(input())
for i in range(1,n+1):
    number=list(map(int,input().split()))
    total=sum(number)/len(number)
    print(f"#{i} {round(total)}")