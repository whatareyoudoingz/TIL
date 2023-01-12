#1
number =input("문자열을 입력하세요 > ")

for i in range(len(number)):
    if number[i] == 'e':
        print(i)
        break
    else:
        continue

#2
number =input("문자열을 입력하세요 > ").split()

call={}
for nu in number:
    if nu not in call:
        call[nu]=1
    else:
        call[nu]+=1

for a,b in call.items():
    print(a,b)

#3
string=input('문자열을 입력하세요 >')
total=[]
for i in string:
    if i == 'e':
        continue
    else:
        total.append(i)
print("".join(total))

#4
string1, string2 =input("문자열을 입력하세요 > ").split()

dic=string1
counts=0
for i in dic:
    if i == string2:
        counts+=1
    else:
        continue

print(counts)


#5
a,b,c =list(input("문자열을 입력하세요 > ").split())
print(f"{a}-{b}-{c}")


#6
##풀이 1
number =int(input("문자열을 입력하세요 > "))

if number < 0:
    print(-1)

else:
    a=number//100
    number=number-a*100
    b=number//10
    number=number-b*10
    c=number
    print(a+b+c)

##풀이 2
number =int(input("양의 정수를 입력하세요 > "))

if number < 0:
    print(-1)

else:
    lis=[]
    for i in range(10,0,-1):
        a=number//(10**i)
        if a != 0:
            number-=a*(10**i)
            lis.append(a)
    lis.append(number)
    print(sum(lis))

##풀이 3
n =int(input("양의 정수를 입력하세요 > "))

if n<0:
    print(-1)
else:
    result=0
    while n>0:
    n//=10
    answer+= n%10

    print(answer)

##풀이 4
n=input()

if n<0:
    print(-1)
else:
    result=0
    for i in n:
        result+=int(i)
    print(result)