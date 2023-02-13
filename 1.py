import sys
sys.stdin = open("input.txt", "r")

for i in range(int(input())):
    n,m=map(int,input().split())
    graph=[]
    for _ in range(m):
        a,b=map(int,input().split())
        graph.append((a,b))
    print(graph)
    print()
    #result=0
    #print(f"{i+1} {result}")