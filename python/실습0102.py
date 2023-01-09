#1
number=int(input('숫자를 입력해주세요 > '))
print(number+10)

#2
food=input('좋아하는 음식을 입력해주세요 > ')
print('좋아하는 음식 :',food)

#3
name=input('이름을 입력해주세요 > ')
year=int(input('태어난 년도를 입력해주세요 > '))
year=2023-year+1
print(f"저의 이름은 {name}이고, 올해 나이는 {year}세 입니다.")

#4
n1=input('첫 번째 문장을 입력해주세요 > ')
n2=input('두 번째 문장을 입력해주세요 > ')
print(n1+n2)

#5
number3=int(input('숫자를 입력해주세요 > '))
print(-number3)

#6
number4=int(input('숫자를 입력해주세요 > '))
number5=int(input('숫자를 입력해주세요 > '))
print('더하기 연산 : ',number4+number5)
print('빼기 연산 : ',number4-number5)
print('곱하기 연산 : ',number4*number5)
print('몫 연산 : ',number4//number5)
print('나머지 연산 : ',number4%number5)

#7
number1=int(input('첫 번째 숫자를 입력해주세요 > '))
number2=int(input('두 번째 숫자를 입력해주세요 > '))
number3=int(input('세 번째 숫자를 입력해주세요 > '))
print(sum([number1,number2,number3])//3)

#8
n1=int(input('첫 번째 숫자를 입력해주세요 > '))
n2=int(input('두 번째 숫자를 입력해주세요 > '))
n3=int(input('세 번째 숫자를 입력해주세요 > '))
n4=int(input('네 번째 숫자를 입력해주세요 > '))
n5=int(input('다섯 번째 숫자를 입력해주세요 > '))
print([n1,n2,n3,n4,n5])

#9
n1=input('문자열을 입력해주세요 > ')
n2=int(input('숫자를 입력해주세요 > '))
print(n1*n2)

#10
n1=int(input('첫 번째 숫자를 입력해주세요 > '))
n2=int(input('두 번째 숫자를 입력해주세요 > '))
n3=int(input('세 번째 숫자를 입력해주세요 > '))
n4=int(input('네 번째 숫자를 입력해주세요 > '))
n5=int(input('다섯 번째 숫자를 입력해주세요 > '))
print(sum([n1,n2,n3,n4,n5]))