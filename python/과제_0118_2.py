# 시험 성적
score=int(input())

if 90<=score<=100:
    print('A')
elif 80<=score<=89:
    print('B')
elif 70<=score<=79:
    print('C')
elif 60<=score<=69:
    print('D')
else:
    print('F') 
    
# 단어 뒤집기
for _ in range(int(input())):
    s=list(input().split())
    answer=''
    for i in s:
        answer+=i[::-1]+" "
    print(answer)

# 열 개씩 끊어 출력하기
s=input()
for i in range(len(s)//10+1):
    print(s[10*i:10*(i+1)])
    
# 나무조각
s=list(map(int,input().split()))
while s != sorted(s):
    for i in range(1,len(s)): # 5개의 개수만큼 반복  
        if s[i]<s[i-1]: #i-1번째 수가 i번째 수보다 크다 면  
            last=s[i-1] #i-1번째 수 저장 
            s[i-1]=s[i] # i-1번째 수와 i번째 수 바꿈 
            s[i]=last 
            print(" ".join(str(j) for j in s))