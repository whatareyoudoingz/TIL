## 반반
for j in range(int(input())):
    ind={}
    s=list(input())
    for i in s:
        ind[i]=s.count(i)
    result=''
    x=list(ind.values())
    if len(set(s))==2:
        if x[0]==2 and x[1]==2 :
            result="Yes"
        else:
            result="No"
    else:
        result="No" 
    print(f"#{j+1} {result}")

## 모음이 보이지 않는 사람
words=['a','e','i','o','u']
for i in range(int(input())):
    word=input()
    for j in words:
        word=word.replace(j , "")
    print(f"#{i+1} {word}")

## 퍼펙트 셔플
for i in range(int(input())):
    n=int(input())
    graph=list(input().split())
    result=''
    if n%2==0:
        for x,y in zip(graph[:n//2],graph[n//2:]):
            result+=x+" "+y+" "
    else:
        for x,y in zip(graph[:n//2+1],graph[n//2+1:]):
            result+=x+" "+y+" "
        result+=graph[:n//2+1][-1]
    print(f"#{i+1} {result}")

## Flatten
for i in range(10):
    n=int(input())
    graph=list(map(int,input().split()))
    for _ in range(n):
        graph[graph.index(max(graph))]-=1
        graph[graph.index(min(graph))]+=1
    print(f"#{i+1} {graph[graph.index(max(graph))]-graph[graph.index(min(graph))]}")
