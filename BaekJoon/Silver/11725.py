from collections import deque

n = int(input()) # 노드 개수 입력
arr = [[] for _ in range(n+1)] # 인접 리스트 배열 생성
visited = [0]*(n+1) # 방문 체크 및 해당 노드의 부모 넣어주기
for _ in range(n-1): # n-1번 돌면서
    a, b = map(int, input().split()) # 두 노드 입력
    arr[a].append(b) # a, b 연결
    arr[b].append(a) # b, a 연결

def bfs(start):
    queue = deque([]) # 큐 생성
    queue.append(start) # 큐에 시작지점 넣기
    visited[start] = 1 # 시작지점 방문체크
    while queue: # 큐가 빌때까지
        size = len(queue) # 큐 사이즈
        for i in range(size): # 큐 사이즈만큼 돌기
            x = queue.popleft() # 현재 노드 큐 맨앞에서 빼기
            for j in arr[x]: # 현재 노드와 연결된 노드들 모두 확인
                if visited[j] == 0: # 현재 노드와 연결된 노드가 방문하지 않았다면
                    visited[j] = x # 연결된 노드에 현재 노드 부모로 체크 및 방문 체크
                    queue.append(j) # 큐에 연결된 노드 넣기

bfs(1) # 1을 루트노드로 bfs 함수 호출
for i in range(2, n+1): # 2~n 노드까지
    print(visited[i]) # 부모 출력