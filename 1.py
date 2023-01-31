import sys
sys.stdin = open("input.txt", "r")

#1
import heapq
heap=[]
for _ in range(int(input())):
    x=int(input())
    if x != 0:
        heapq.heappush(heap,x)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)

#2
s=set()
cnt=0
for word in words:
    if word in s :
        cnt+=1
print(cnt)

