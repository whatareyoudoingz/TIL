T=int(input())
for i in range(T):
    total=0
    numbers=list(map(int,input().split()))
    for number in numbers:
        if number%2!=0:
            total+=number
    print(f"#{i+1} {total}")