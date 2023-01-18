import sys
sys.stdin = open("input.txt", "r")
s=list(map(int,input().split()))
while s != sorted(s):
    for i in range(1,len(s)): 
        if s[i]<s[i-1]:
            last=s[i-1] 
            s[i-1]=s[i]
            s[i]=last 
            print(" ".join(str(j) for j in s))
