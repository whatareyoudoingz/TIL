for k in range(int(input())):
    length=list(map(int,input().split()))
    for i in set(length):
        if length.count(i) == 1 or length.count(i)==3:
            print(f"#{k+1} {i}")