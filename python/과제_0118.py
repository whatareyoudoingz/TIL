# 유학 금지
s=input()
answer=''
for i in s:
    if i not in "CAMBRIDGE":
        answer+=i
print(answer)

# 문자열 반복
n=int(input())
for _ in range(n):
    a,b = input().split()
    for i in range(len(b)):
        print(b[i]*int(a),end='')
    print()

# 팰린드롬인지 확인하기
s=input()
print( 1 if s == s[::-1] else 0)

# 태보태보 총난타
a,b=input().split("(^0^)")
print(a.count("@"),b.count("@"))

#크로아티아 알파벳
s=input()
lis=['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in lis:
    if i in s:
        s=s.replace(i," ")
print(len(s))

# 알파벳 찾기
s=input()
lis=[-1 for _ in range(26)]
for i in s:
    if lis[ord(i)-97] == -1 :
        lis[ord(i)-97] = s.find(i)
for a in lis:
    print(a , end=' ')