# 삼각형 외우기
lis=[]
for _ in range(3):
    lis.append(int(input()))

dic={}
for i in set(lis):
    dic[i]=lis.count(i)

if sum(lis)==180:
    if len(dic.keys())==1:
        print("Equilateral")
    elif len(dic.keys())==2:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")

# 세탁소 사장 동혁
coin=[25,10,5,1]
for _ in range(int(input())):
    money=int(input())
    for i in coin:
        print(money//i, end=" ")
        money%=i
    print()

# 피시방 알바
seat=list(range(1,101))
n, total=int(input()) , 0
numbers=list(map(int,input().split()))
for number in numbers:
    if number in seat:
        seat.remove(number)
    else:
        total+=1
print(total)

# 제로
total=[]
for _ in range(int(input())):
    money=int(input())
    if money != 0:
        total.append(money)
    else:
        total.pop()
print(sum(total))

# 카드1
total=list(range(1,int(input())+1))
lis=[]
while len(total)!=1:
    lis.append(total.pop(0))
    total.append(total.pop(0))
print(*lis, total[0])

## deque 사용해서 풀어보기


##수업 전 풀이
total=[i for i in range(1,int(input())+1)]
lis=[]
while len(total)!=1:
    lis.append(total[0])
    total.pop(0)
    t=total[0]
    total.pop(0)
    total.append(t)
print(" ".join(str(i) for i in lis+total))

# 괄호
for _ in range(int(input())):
    string, lis, i =input(), [], 0
    while i != len(string):
        if string[i] == '(':
            lis.append(string[i])
        else:
            if '(' in lis:
                lis.pop()
            else:
                break
        i+=1
    if i == len(string) and len(lis)==0:
        print("YES")
    else:
        print("NO")

## 다른 사람 풀이 (신박함)
for i in range(int(input())):
    ps = input()
    while True:
        pst = ps
        ps = ps.replace('()', '')
        if pst == ps:
            break
    if len(ps) == 0:
        print('YES')
    else:
        print('NO')

## for else문 활용
### for문이 break로 끝나면 else블럭 실행z , 안 끝나면 else블럭 실행o
for _ in range(int(input())):
    string, lis =input(), []
    for i in string:
        if i == '(':
            lis.append(i)
        else:
            if '(' in lis:
                lis.pop()
            else:
                break
else:
    if len(lis)==0:
        print("YES")
    else:
        print("NO")