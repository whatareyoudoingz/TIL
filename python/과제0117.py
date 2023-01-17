# 10818 최소, 최대
n=int(input())
lis=list(map(int,input().split()))

print(min(lis),max(lis))

#11720 숫자의 합
n=int(input())
number=list(map(int,input()))

total, i=0, 0
while i!=n:
    total+=number[i]
    i+=1

print(total)

# 수 정렬하기
## 숏코딩
number=[int(input()) for _ in range(int(input())) ]

for i in sorted(number):
    print(i)
## 코드 리뷰
n=int(input())
number=[]
for _ in range(n):
    number.append(int(input()))
for i in sorted(number):
    print(i)

# 최댓값
## 숏코딩
number=[int(input()) for _ in range(9)]
a=sorted(number)[-1]
print(a,number.index(a)+1,sep="\n")

## 코드 리뷰
number=[]
for _ in range(9):
    number.append(int(input()))
    number1=sorted(number)
print(number1[-1],number.index(number1[-1])+1,sep='\n')