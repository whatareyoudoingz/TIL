#1
n=int(input())
print(n)

#2
print(" ".join(input().split()))

#3
n=int(input())
for i in range(1,n+1):
    print(i)

#4
number=input().split()
print(" ".join(i for i in number))

#5
a,b=map(int,input().split())
print(a,b)

#6
string=input().split()
print(" ".join(string))

#7
b=int(input())
print(b)

for i in range(1,b+1):
    a,b,c=map(int,input().split())
    print(a,b,c)

#8
b=int(input())
print(b)

for i in range(1,b+1):
    print(" ".join(i for i in input().split()))