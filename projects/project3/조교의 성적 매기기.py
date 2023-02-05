for q in range(int(input())):
    n,k=map(int,input().split()) 
    grade=['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
    per=n//10 #비율 

    # 정렬해서 비율대로 자르자.
    student=[]
    for _ in range(n):
        a,b,c=map(int,input().split())
        total=a*0.35+b*0.45+c*0.2
        student.append(total)

    number=0
    total=sorted(student,reverse=True)
    dic=dict()
    for i in range(0,n,per): 
        for j in range(0,per):
            dic[total[i+j]]=grade[number]
        number+=1
    print(f"#{q+1} {dic[student[k-1]]}")