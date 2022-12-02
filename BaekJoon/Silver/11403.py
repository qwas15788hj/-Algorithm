from collections import deque

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split()))) #간선 정보 입력

def bfs(start): #시작 지점부터 간선을 확인하며 연결되어 있는 곳 찾는 bfs
    queue = deque([])
    queue.append(start) #시작점 추가
    while queue:
        x = queue.popleft() #현재 지점 뽑고
        for i in range(n):
            if arr[x][i]==1 and not visited[i]: #현재 지점과 연결(1)되어 있고, 방문하지 않았다면
                queue.append(i) #추가
                visited[i] = True #방문체크

for i in range(n):
    visited = [False]*n
    bfs(i)
    for i in range(n):
        if visited[i]:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()