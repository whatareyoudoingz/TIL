T=int(input())
for t in range(T):
    lis=list(map(str,range(10)))
    n=int(input())
    i=0
    while len(lis)!=0:
        p=n*(i+1)
        for j in str(p):
            if  j in lis:
                lis.remove(j)
        i+=1
    print(f"#{t+1} {i*n}")   