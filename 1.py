import sys
sys.stdin = open("input.txt", "r")


lis_x=[]
lis_y=[]

for _ in range(3):
    a,b=input().split()
    lis_x.append(a)
    lis_y.append(b)

for k in lis_x:
    if lis_x.count(k)<2:
        x=k
for q in lis_y:
    if lis_y.count(q)<2:
        y=q
print(x,y)


    
        
    