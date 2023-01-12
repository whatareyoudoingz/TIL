# 홀수만 더하기
T=int(input())
for i in range(T):
    total=0
    numbers=list(map(int,input().split()))
    for number in numbers:
        if number%2!=0:
            total+=number
    print(f"#{i+1} {total}")

# 연원일 달력
T=int(input())

for i in range(T):
    numbers=input()
    year=numbers[:4]
    month=numbers[4:6]
    day=numbers[6:]
    if int(month) in range(1,13):#월 있음
        if int(month) in [1,3,5,7,8,10,12]:
            if int(day) in range(1,32):
                result=f"{year}/{month}/{day}"
        elif int(month) in [4,6,9,11]:
            if int(day) in range(1,31):
                result=f"{year}/{month}/{day}"
        else:
            if int(day) in range(1,29):
                result=f"{year}/{month}/{day}"
            else:
                result=-1
    else:
        result=-1
    print(f"#{i+1} {result}")

# 서랍의 비밀번호
p,k=map(int,input().split())
print(p-k+1)

# 간단한 N의 약수
n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")

# 새로운 불면증 치료법
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