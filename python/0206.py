# 행복한지 슬픈지
string=input()
cnt=[string.count(':-('),string.count(':-)')]
if cnt[0]==0 and cnt[1]==0:
    print("none")
elif cnt[0]==cnt[1]:
    print("unsure")
elif cnt[0]<cnt[1]:
    print("happy")
else:
    print("sad")

# 지능형 기차
person=0
max_person=[]
for i in range(4):
    out_person,in_person=map(int,input().split())
    person+=(-out_person+in_person)
    max_person.append(person)
print(max(max_person))

# 바이러스
T=int(input())
graph=[list() for _ in range(T)]
for _ in range(int(input())):
    a,b=map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

visited=[False]*T
cnt=0

def dfs(start):
    global cnt
    stack=[start]
    visited[start]=True
    while stack:
        cur=stack.pop()
        for j in graph[cur]:
            if not visited[j]: 
                cnt+=1
                visited[j]=True
                stack.append(j)

dfs(0)
print(cnt)

# 섬의 개수
