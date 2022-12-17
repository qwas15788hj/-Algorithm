import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split()) # 사다리 수 n, 뱀의 수 m 입력
arr = [i for i in range(101)] # 100번까지의 보드판
for _ in range(n): # 사다리 입력
    x, y = map(int, input().split()) # x, y 입력
    arr[x] = y # x => y로 이동하기에 x번째 y로 변경
for _ in range(m): # 뱀 입력
    u, v = map(int, input().split()) # u, v 입력
    arr[u] = v # u => v로 이동하기에 u번째 v로 변경

def bfs(start): # 주사위를 통해 이동하는 함수 bfs 이용
    queue = deque([]) # 큐 생성
    queue.append(start) # 큐에 시작점 넣기
    time = 0 # 시간 체크
    visited = [False]*101 # 방문체크 (시간복잡도 줄이기)
    while queue: # 큐가 빌때까지
        size = len(queue) # 큐 크기
        for i in range(size): # 큐 크기만큼 돌기
            x = queue.popleft() # 현재위치 뽑기 (큐 맨앞)
            if arr[x] == 100: # 현재 위치가 100을 가리키면(arr[100])
                return time # 현재 시간 리턴
            for j in range(1, 7): # 주사위 굴리기 1~6
                nx = x+j # 이동할 위치 = 현재 위치+주사위 수
                if 0<=nx<101 and not visited[nx]: # 이동할 위치가 범위 안에 있고, 방문하지 않았다면
                    queue.append(arr[nx]) # 이동할 위치의 이동 위치를 큐에 넣기 (사다리와 뱀 위치때문) ex) 32 => 62로 이동
                    visited[nx] = True # 이동한 위치 방문 체크
                    visited[arr[nx]] = True # 이동한 위치의 이동 위치 방문 체크
        time += 1 # 시간 증가

print(bfs(1)) # 1번에서 시작하는 bfs함수 호출 후 시간 출력