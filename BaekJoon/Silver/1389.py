from collections import deque

n, m = map(int, input().split()) # 입력
answer = [0]*(n+1) # 사람 별 걸리는 케빈 베이커 거리
answer[0] = 1e9 # 0은 max설정
arr = [[] for _ in range(n+1)] # 사람 별 연결 간선 체크
for _ in range(m): # 입력
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def bfs(start): # 사람마다 다른 사람과의 거리 체크 함수
    queue = deque()
    queue.append(start) # 큐에 시작 지점 넣기
    visited[start] = -1 # 시작 지점
    count = 1 # 단계
    while queue:
        size = len(queue) # 큐의 사이즈
        for i in range(size): # 큐 사이즈 만큼
            x = queue.popleft() # 큐에서 뽑고
            for j in arr[x]: # 현재 지점에 연결 되어 있는 모든 간선 체크
                if not visited[j]: # 방문 안했다면
                    queue.append(j) # 큐에 넣고
                    visited[j] = count # 걸린 시간 체크
        count += 1 # 시간 증가

    cnt = 0 # 모든 사람 걸린 시간 총 시간
    for i in range(1, n+1): # 1~n명까지
        if i != start: # 나를 제외한
            cnt += visited[i] # 걸린 시간 증가
    answer[start] = cnt # 내가 걸린 시간에 넣기

for i in range(1, n+1): # 1~n까지 돌면서
    visited = [0]*(n+1) # 걸린 시간 초기화
    bfs(i) # bfs함수 돌기

print(answer.index(min(answer))) # 걸린 시간 중 가장 적게 걸린 시간의 인덱스 출력