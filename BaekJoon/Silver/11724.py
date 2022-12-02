from collections import deque

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)] #인접리스트
for _ in range(m): #인접리스트 만들기
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def bfs(start): #인접리스트를 통해 연결선을 만드는 함수
    queue = deque([])
    queue.append(start) #시작지점 큐에 넣기
    visited[start] = True #시작점 방문체크
    while queue: #큐 돌면서
        x = queue.popleft() #확인할 지점 꺼내기
        for i in arr[x]: #현재지점과 연결되어있는 다른 지점을 돌면서
            if not visited[i]: #해당 지점이 방문 안했다면
                queue.append(i) #큐에 넣고
                visited[i] = True #방문체크

visited = [False]*(n+1)
count = 0
for i in range(1, n+1): #1~n까지 돌면서
    if not visited[i]: #방문 안했다면
        bfs(i) #bfs 돌고
        count += 1 #카운트 증가

print(count)