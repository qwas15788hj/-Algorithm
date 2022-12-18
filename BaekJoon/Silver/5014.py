from collections import deque

f, s, g, u, d = map(int, input().split()) # f, s, g, u, d 입력

def bfs(start): # 해당 층 가는데 걸리는 시간 구하는 함수 (bfs 사용)
    global f, g, u, d # f, g, u, d 사용하기 위해 전역변수
    queue = deque([]) # 큐 생성
    queue.append(start) # 큐에 현재 위치 넣기
    visited = [0]*(f+1) # 방문했는지와 도착한 층에 몇 초 걸렸는지 저장하는 배열
    visited[start] = 1 # 시작지점 1초
    while queue: # 큐 빌때까지
        size = len(queue) # 큐 크기
        for i in range(size): # 큐 크기만큼 돌면서
            x = queue.popleft() # 현재위치(큐에서 뽑기)
            nx = x+u # 위로 올라갈때: 현재위치+u
            if 0<nx<=f and visited[nx]==0: # 이동할 위치가 범위안에 있고, 방문 안했다면
                queue.append(nx) # 큐에 이동할 위치 넣고
                visited[nx] = visited[x]+1 # 이전위치에서 1초 더 걸리고 방문체크
            nx = x-d # 아래로 내려갈때: 현재위치-d
            if 0<nx<=f and visited[nx]==0: # 이동할 위치가 범위안에 있고, 방문 안했다면
                queue.append(nx) # 큐에 이동할 위치 넣고
                visited[nx] = visited[x]+1 # 이전위치에서 1초 더 걸리고 방문체크

    if visited[g]==0: # 목적위치에 도달 못했으면
        return "use the stairs" # 해당 문구 리턴
    else: # 목적위치에 도달했다면
        return visited[g]-1 # 도달한 시간 리턴 (시작이 1초였으므로 -1)

print(bfs(s)) # 시작지점넣고 bfs함수 호출 출력