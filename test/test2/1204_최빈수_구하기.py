T=int(input())
for _ in range(T):
    n=int(input())
    number=list(map(int,input().split()))
    dic=dict()
    for i in set(number):
        dic[i]=number.count(i)
    for a,b in dic.items():
        if b == max(dic.values()):
            print(f"#{n} {a}")
    