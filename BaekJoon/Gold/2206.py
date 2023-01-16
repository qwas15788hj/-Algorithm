from collections import deque

n, m = map(int, input().split()) # n, m 입력
arr = [] # 맵 배열
for i in range(n): # 맵 입력
    arr.append(list(map(int, input())))

visited = [[[0]*2 for _ in range(m)] for _ in range(n)] # 방문 배열, 3차원 0, 1은 벽을 부쉈는지 확인
visited[0][0][0] = 1 # 시작지점 방문처리

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, z): # 최단거리 확인 함수
    queue = deque()
    queue.append([x, y, z]) # 큐에 현재 위치 x, y와 벽 부순 수 z 입력
    while queue: # 큐 돌면서
        nx, ny, nz = queue.popleft() # 꺼내고
        if nx==n-1 and ny==m-1: # 꺼낸 위치가 마지막 위치면
            return visited[nx][ny][nz] # 방문 횟수 리턴
        for i in range(4): # 4방향 돌면서
            mx = nx+dx[i]
            my = ny+dy[i] # 다음 이동할 위치
            if 0<=mx<n and 0<=my<m: # 다음 갈 위치가 범위 안에 있고
                if arr[mx][my]==1 and nz==0: # 다음 위치가 벽이면서 현재까지 오면서 벽을 안만났을 경우 부수고 이동 가능
                    visited[mx][my][1] = visited[nx][ny][0] + 1 # 다음 위치(부순 수 1) = 현재 위치(부순 수 0) + 1
                    queue.append([mx, my, 1]) # 다음 위치 (부순 수 1) 큐에 넣기
                elif arr[mx][my]==0 and visited[mx][my][nz]==0: # 다음 위치가 이동 가능한 위치면서 방문한적 없을 경우
                    visited[mx][my][nz] = visited[nx][ny][nz] + 1 # 다음 위치 = 현재 위치 + 1
                    queue.append([mx, my, nz]) # 큐에 넣기
    return -1 # 도달 못할시 -1 리턴

print(bfs(0, 0, 0))