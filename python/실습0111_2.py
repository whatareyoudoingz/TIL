#2047
print(input().upper())

#2025
print(sum(range(1,int(input())+1)))

#1936
a,b=map(int,input().split())

if (a,b) in [(1,3),(2,1),(3,2)]:
    print("A")
else:
    print("B")

## 숏코딩 
print("A" if (a,b) in [(1,3),(2,1),(3,2)] else "B")

#2027
a,b="+","#"
for i in range(5):
    print(f"{a*(i)}{b}{a*(4-i)}")

#2058
i=0
for j in str(input()):
    i+=int(j)
print(i)

#2019
for i in range(int(input())+1):
    print(2**(i),end=" ")