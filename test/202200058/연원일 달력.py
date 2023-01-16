T=int(input())

for i in range(T):
    numbers=input()
    year=numbers[:4]
    month=numbers[4:6]
    day=numbers[6:]
    if int(month) in range(1,13):#월 있음
        if int(month) in [1,3,5,7,8,10,12]:
            if int(day) in range(1,32):
                result=f"{year}/{month}/{day}"
        elif int(month) in [4,6,9,11]:
            if int(day) in range(1,31):
                result=f"{year}/{month}/{day}"
        else:
            if int(day) in range(1,29):
                result=f"{year}/{month}/{day}"
            else:
                result=-1
    else:
        result=-1
    print(f"#{i+1} {result}")