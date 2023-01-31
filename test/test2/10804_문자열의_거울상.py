for k in range(int(input())):
    number=list(input()[::-1])
    answer=""
    for i in number:
        if i == 'b':
            answer+='d'
        elif i == 'd':
            answer+='b'
        elif i == 'p':
            answer+='q'
        elif i == 'q':
            answer+='p'
    print(f"#{k+1} {answer}")