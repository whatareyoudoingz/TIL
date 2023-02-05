answer=''
for a in range(10):
    n=int(input())
    string, lis , i=input() , [], 0
    dic={']':'[',')':'(','}':'{','>':'<'}
    while i != n:
        if string[i] in dic.values(): #열린 괄호면
            lis.append(string[i]) #추가
        else: #닫힌 괄호면
            if dic[string[i]] == lis[-1]: #열린괄호가 있는지 확인 
                lis.pop()
            else:  #열린 괄호가 없으면 반복문 끝!
                break
        i+=1
    if i == n and len(lis)==0:  #다 완수했거나, 내용이 없다면
        answer=1
    else: 
        answer=0
    print(f"#{a+1} {answer}")