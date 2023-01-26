for k in range(int(input())):
    number=input()
    if '-' in number:
        number=number.replace('-','')
    if number[0] in ['3','4','5','6','9'] and len(number)==16:
        result=1
    else:
        result=0

    print(f"#{k+1} {result}")