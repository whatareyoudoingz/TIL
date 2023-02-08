# 막대기
import sys
n=int(sys.stdin.readline())
tall=list(int(sys.stdin.readline()) for _ in range(n))
result=1
maxx=tall[-1]
for i in range(n-1,-1,-1):
    if tall[i]>maxx:
        maxx=tall[i]
        result+=1
print(result)

## 다른 분 풀이 (한선진 님)
import sys 
a = int(input())
b = []
count = 1
for i in range(a):
    b.append(int(sys.stdin.readline()))
num = b.pop()
for j in range(a-1):
    number = b.pop()
    if number > num :
        count += 1
        num = number
print(count)

# 덩치
a = int(input())
c = []
for i in range(a):
    b = list(map(int,input().split()))
    c.append(b)

for i in c:
    result = 1
    for j in c:
        if i[0] < j[0] and i[1] < j[1]:
            result += 1
    print(result, end=" ")

# 킹
move = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1], 'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]}
king, stone, N = input().split()
k = list(map(int, [ord(king[0]) - 64, king[1]]))
s = list(map(int, [ord(stone[0]) - 64, stone[1]]))
for i in range(int(N)):
    m = input()
    x = k[0] + move[m][0]
    y = k[1] + move[m][1]
    if 0 < x <= 8 and 0 < y <= 8:
    if s[0] == x and s[1] == y:
        x1 = s[0] + move[m][0]
        y1 = s[1] + move[m][1]
        if 0 < x1 <= 8 and 0 < y1 <= 8:
        k = [x, y]
        s = [x1, y1]
    else:
        k = [x, y]

print(f'{chr(k[0] + 64)}{k[1]}')
print(f'{chr(s[0] + 64)}{s[1]}')