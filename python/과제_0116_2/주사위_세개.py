a,b,c=list(map(int,input().split()))

n1=a==b
n2=a==c
n3=b==c
total=n1+n2+n3
if total == 3:
        print(10000+a*1000)
elif total == 1:
	if a==b or a==c:
        print(1000+a*100)
	else:
        print(1000+b*100)
elif total == 0:
	print(max(a,b,c)*100)