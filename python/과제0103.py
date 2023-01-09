#1
n=int(input('정수를 입력하세요 > '))
if n > 0:
    print('True')
else:
    print('False')

#2
n1=int(input('첫 번째 정수를 입력하세요 > '))
n2=int(input('두 번째 정수를 입력하세요 > '))
if n1 ==n2:
	print("False")
else:
	print(max(n1,n2))

#3
n1=int(input('정수를 입력하세요 > '))
if 1 < n1 < 10:
	print("True")
else:
	print("False")

#4
n1=int(input('정수를 입력하세요 > '))
if 0 < n1 and n1%2==0:
	print("True")
else:
	print("False")

#5
n1=int(input('정수를 입력하세요 > '))

if 0 > n1 or n1 >100: 
	print("에러")
elif n1 >=60:
	print('합격')
else:
	print("불합격")

#6
n1=input('문자열을 입력하세요 > ')
for char in n1[::-1]:
	print(char)

n1=list(input('문자열을 입력하세요 > '))
for char in range(len(n1)-1,-1,-1):
	print(n1[char])

#7
n1=int(input('첫 번째 정수를 입력하세요 > '))
n2=int(input('두 번째 정수를 입력하세요 > '))
if n1==n2:
	print("False")
else:
	for i in range(min(n1,n2)+1,max(n1,n2)):
		print(i)

#8
n1=int(input('첫 번째 정수를 입력하세요 > '))
n2=int(input('두 번째 정수를 입력하세요 > '))
if n1==n2:
	print("False")
else:
	for i in range(max(n1,n2)-1,min(n1,n2),-1):
		print(i, end=' ')
        
#9
n1=int(input('정수를 입력하세요 > '))

if n1 < 1 :
	print("False")
else:
	for i in range(1,n1):
		if i%2==1:
			print(i)

#10
for i in range(2,10):
	for j in range(2,10):
		print(f"{i} X {j} = {i*j}")