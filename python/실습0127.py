# 세 수
number=list(map(int,input().split()))
print(sorted(number,reverse=True)[1])

# 고무오리 디버깅
massage=input()
lis=[]
while True:
    massage=input()
    if "고무오리 디버깅 끝"==massage:
        break
    if massage == '문제':
        lis.append(massage)
    else:
        if lis: 
            lis.pop()
        else:
            lis.extend(["문제","문제"])
print("고무오리야 사랑해" if len(lis)==0 else "힝구")

## 왜 안돼??
massage=input()
lis=[]
while "고무오리 디버깅 끝"!=massage:
    massage=input()
    if massage == '문제':
        lis.append(massage)
    else:
        if lis: 
            lis.pop()
        else:
            lis.extend(["문제","문제"])
print("고무오리야 사랑해" if len(lis)==0 else "힝구")

# 대칭 차집합
a,b=map(int,input().split())
A=set(map(int,input().split()))
B=set(map(int,input().split()))
print(len(A^B))

# 나머지
total=set(int(input())%42 for _ in range(10))
print(len(total))

# 단어 정렬
lis=set(input() for _ in range(int(input())))
lis=sorted(sorted(lis,reverse=False),key= lambda x : len(x))
print(*lis, sep='\n')

# 절댓값 힙
## 시간 초과 나왔습니다...
import sys
import heapq
heap=list()
for _ in range(int(sys.stdin.readline().strip())):
    n=int(sys.stdin.readline().strip())

    if n!=0:
        heapq.heappush(heap,n)
    else:
        heap.sort(key=lambda x : abs(x))
        if len(heap) >= 1:
            dic=set(heap)
            cnt=heap[0]
            for i in dic:
                if abs(i)==heap[0] and i <heap[0]:
                    cnt=i
            print(cnt)
            heap.remove(cnt)

        elif len(heap)==0:
            print(0)
## 정답
import sys
import heapq
T = int(input()) # 테스트 케이스 수
li = []
for _ in range(T):
    a = int(sys.stdin.readline())
    if a != 0:
        heapq.heappush(li, (abs(a), a))
    else:
        if li:
            print(heapq.heappop(li)[1])
        else:
            print(0)


## 정답
import sys
import heapq
heap=list()
for _ in range(int(input())):
    n=int(sys.stdin.readline().strip())

    if n!=0:
        heapq.heappush(heap,(abs(n),n))
    else:
        heap.sort(key=lambda x : abs(x))
        if len(heap) >= 0:
            ???

        elif len(heap)==0:
            print(0)