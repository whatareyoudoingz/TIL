import sys
sys.stdin = open("input.txt", "r")

def han(a):
    global result

    a=list(str(i))
    if len(a)==1 or len(a)==2:
        result+=1
    for j in range(len(a)):
        if j==len(a)-1:
            a.remove(a[-1]) 
        else:
            a[j]=int(a[j+1])-int(a[j])

    for k in range(len(a)):
        if k == len(a)-1 or a[k+1]!=a[k]:
            break
        result+=1
    return result


x=int(input())
result=0
for i in range(1,x+1):
    han(i)
print(result)



	

