for k in range(int(input())):
    n=int(input())
    people=list(map(int,input().split()))
    total=0
    for i in people:
        if i <= sum(people)/n:
            total+=1
    print(f"#{k+1} {total}")