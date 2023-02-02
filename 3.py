import sys
sys.stdin = open("input_1.txt", "r")

m,n=7, 7

## 리스트 초기화

graph=[[] for _ in range(n)] 

## 연결
for _ in range(m):
    v1,v2=map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

print(graph)