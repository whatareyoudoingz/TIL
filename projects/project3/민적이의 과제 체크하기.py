for i in range(int(input())):
    n,k=map(int,input().split())
    member=[i for i in range(1,n+1)]
    for j in list(map(int,input().split())):
        member.remove(j)
    print(f"#{i+1}", " ".join(str(m) for m in member))