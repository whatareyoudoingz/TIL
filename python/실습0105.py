#1
n1=input('문자열을 입력하세요 > ')

count=0
for word in n1:
    if 'e' == word:
        count+=1
print(count)

#2
n1=input('문자열을 입력하세요 > ')
mo=['a','e','i','o','u','A','E','I','O','U']

count=0
for word in n1:
    if word in mo:
        count+=1
print(count)

#3
dict_variable = {
    "이름": "정우영",
    "생년": "2000",
    "회사": "하이퍼그로스",
}

### 이하 문제 해결 코드 작성
print(f"나이 : {2023-int(dict_variable['생년'])+1}세")

#4
name=input('이름을 입력하세요 >') 
call=input('전화번호를 입력하세요 >') 
address=input('거주지를 입력하세요 >')

person={'이름':name, '전화번호':call, '거주지':address}
print(person)

for i,j in person.items():
    print(f"{i} : {j}")

#5
name=input('이름을 입력하세요 >') 
call=input('전화번호를 입력하세요 >') 
address=input('거주지를 입력하세요 >')

person={'이름':name, '전화번호':call, '거주지':address}

calling={}
calling['정우영']=person
print(calling)

#6
n1=input('문자열을 입력하세요 >') 

i=0
dic={}
while i < len(n1):
    if n1[i] not in dic:
        dic[n1[i]]=1
    else:
        dic[n1[i]]+=1
    i+=1

for i,j in dic.items():
    print(i,j)