for i in range(int(input())):
    n,m=map(int,input().split())
    graph=[list(map(int,input().split())) for _ in range(n)] #파리 분포도

    #가장 큰 분포도를 찾아보자!
    total=0
    answer=[]
    for a in range(n-m+1): # 움직임 제한
        for b in range(n-m+1):
            total=0
            for x in range(m): # 파리채
                for y in range(m):
                    total+=graph[a+x][b+y]
            answer.append(total)
        
    print(f"#{i+1} {max(answer)}")