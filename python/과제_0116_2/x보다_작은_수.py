##1
n ,x=map(int,input().split())
a=list(map(int,input().split()))
answer=[]
for number in a:
    if number < x:
        answer.append(number)
    else:
        continue
print(" ".join(str(i) for i in answer))

##2 숏코딩
n, v=map(int,input().split())
lis=list(map(int,input().split()))

print(" ".join(str(i) for i in lis if i < v))

## 다른 풀이(지현님)
N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in A:
    if i < X:
        print(i, end=' ')