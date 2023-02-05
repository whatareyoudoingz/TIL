for i in range(int(input())):
    n,k=map(int,input().split())
    graph=[list(map(int,input().split())) for _ in range(n)]
    total=0
    for x in range(n):
        count=0
        for y in range(n):
            if graph[x][y]==1: #흰색
                if y==n-1: #마지막
                    count+=1
                    if count==k: 
                        total+=1
                else:
                    count+=1
            else: #검은색
                if count==k: 
                    total+=1
                count=0

    for y in range(n):
        count=0
        for x in range(n):
            if graph[x][y]==1: #흰색
                if x==n-1: #마지막
                    count+=1
                    if count==k: 
                        total+=1
                else:
                    count+=1
            else: #검은색
                if count==k: 
                    total+=1
                count=0
    print(f"#{i+1} {total}")