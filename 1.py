import sys
sys.stdin = open("input.txt", "r")

x=int(input())
dic=[[0 for _ in range(x) ] for _ in range(x) ]
for i in range(x):
    for j in range(x):
        dic[i][j]=f"{i+1} / {j+1}"
print(dic)

a,b=0,0
q=1
while  q < x+1:
    print(a,b)
    if q==4:
        break
    if q==1:
        a=b=0
        q+=1
    elif q==2:
        a,b=a,b+1
        q+=1
    else:
        if a==0 and b!=0:
            while b!=0:
                a,b=a+1,b-1
                q+=1
            if b==0:
                a,b=a+1,b
                q+=1
                break
        elif b==0 and a!=0:
            while True:
                if a==0:
                    a,b=a,b+1
                    q+=1
                    break
                a,b=a-1,b+1
                q+=1

print(a,b)
print(dic[a][b])