for k in range(int(input())):
    number=list(map(int,input().split()))
    answer=[]
    for i in range(len(number)):
        if i%2==0:
            answer.append(number[i]*2)
        else:
            answer.append(number[i])
    if sum(answer)%10 == 0:
        result=0
    else:
        result=10*(sum(answer)//10+1)-sum(answer)
    print(f"#{k+1} {result}")