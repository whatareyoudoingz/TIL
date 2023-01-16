# 1
a,b=map(int,input().split())
print(a+b)

#2
a=int(input())
b=int(input())
print(a+b)

#3
a=int(input())
answer=[]
for i in range(a):
    n1,n2=map(int,input().split())
    answer.append(n1+n2)
for i in answer:
	print(i)

#4
a=int(input())
for _ in range(a):
    b,c=map(int,input().split(','))
    print(b+c)

#5
T=int(input())
for i in range(T):
    b,c=map(int,sys.stdin.readline().split())
    print(f"Case #{i+1}: {b+c}")

#6
T=int(input())
for i in range(T):
    b,c=map(int,sys.stdin.readline().split())
    print(f"Case #{i+1}: {b} + {c} = {b+c}")