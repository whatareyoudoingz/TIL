## 아이디어 : 입력 리스트를 점수 저장소로 사용하자!

#입력
n=int(input())
array=list(map(int,input().split()))

# 알고리즘
for i in range(n):
    if i == 0 : #맨 처음에는 그대로 둬라
        continue
    if array[i] == 1: # 1이라면
        if array[i -1] != 0 : # 그 전 문제를 맞췄다면 # 연속으로 맞췄을 경우
            array[i] = array[i-1]+1 #연속적으로 1을 더해줘라

#출력
print(sum(array)) #합을 출력해라