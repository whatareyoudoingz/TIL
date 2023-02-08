import sys
sys.stdin = open("input_1.txt", "r")

n=int(sys.stdin.readline())
tall=list(int(sys.stdin.readline()) for _ in range(n))
result=1
maxx=tall[-1]
for i in range(n-1,-1,-1):
    if tall[i]>maxx:
        maxx=tall[i]
        result+=1

print(result)

    