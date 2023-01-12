#2029
n=int(input())
for i in range(1,n+1):
    a,b=map(int,input().split())
    print(f"#{i} {a//b} {a%b}")

#2071
n=int(input())
for i in range(1,n+1):
    number=list(map(int,input().split()))
    total=sum(number)/len(number)
    print(f"#{i} {int(round(total,0))}")


#1938
a,b=map(int,input().split())
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))

#2046
print("#"*int(input()))

#2068
n=int(input())
for i in range(1,n+1):
    number=list(map(int,input().split()))
    print(f"#{i} {max(number)}")
    