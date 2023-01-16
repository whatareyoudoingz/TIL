## 1
n=int(input())

total=0
for _ in range(n):
    ans=int(input())
    total+=ans
if total > (n//2):
    print("Junhee is cute!" )
else:
    print("Junhee is not cute!")

##2 숏코딩
n=int(input())
total=0
for _ in range(n):
    ans=int(input())
    total+=ans
print("Junhee is cute!" if total > (n//2) else "Junhee is not cute!")