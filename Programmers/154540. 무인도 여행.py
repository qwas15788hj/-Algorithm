from collections import deque

def solution(maps):
    answer = []
    n = len(maps)  # 세로
    m = len(maps[0])  # 가로

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False] * m for _ in range(n)]  # 방문처리

    for i in range(n):
        for j in range(m):  # 맵 돌면서
            if maps[i][j] != "X" and not visited[i][j]:  # 땅이고 방문 안했을 경우
                queue = deque()
                queue.append([i, j])  # 첫 시작점 큐에 넣기
                cnt = int(maps[i][j])  # 첫 시작점 식량
                visited[i][j] = True  # 첫 시작점 방문 처리
                while queue:  # 큐 돌면서
                    size = len(queue)
                    for _ in range(size):
                        x, y = queue.popleft()  # 좌표 꺼내고
                        for j in range(4):  # 상하좌우 탐색
                            nx = x + dx[j]
                            ny = y + dy[j]  # 다음 이동 위치
                            # 다음 이동 위치가 범위 안에 있고, 육지고, 방문 안했을 경우
                            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != "X" and not visited[nx][ny]:
                                cnt += int(maps[nx][ny])  # 식량 더해주고
                                visited[nx][ny] = True  # 방문 처리
                                queue.append([nx, ny])  # 큐에 추가
                answer.append(cnt)

    if len(answer) == 0:
        answer.append(-1)
    answer.sort()

    return answer