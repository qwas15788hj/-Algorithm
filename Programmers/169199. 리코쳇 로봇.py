from collections import deque


def solution(board):
    answer = 0
    n = len(board)  # 세로 5
    m = len(board[0])  # 가로 7
    visited = [[False] * m for _ in range(n)]  # 방문 처리

    # 시작 지점 구하기
    start_x, start_y = 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                start_x, start_y = i, j  # 세로, 가로

    # 4 방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 큐 이용
    queue = deque([])
    queue.append([start_x, start_y])
    visited[start_x][start_y] = True
    flag = False
    # 큐 돌면서
    while queue:
        size = len(queue)  # 큐 크기로 돌아야 모든 위치 4방향 조회 가능
        for j in range(size):  # 큐 크기로 돌면서
            x, y = queue.popleft()  # 뽑고
            if board[x][y] == "G":  # 도착 지점이면
                flag = True  # 체크
                break
            for i in range(4):  # 4방향 돌면서
                nx, ny = x, y
                while True:  # 현재 방향으로 한 칸씩 계속 이동
                    nx += dx[i]
                    ny += dy[i]
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 다음 위치가 범위 밖이고
                        if not visited[nx - dx[i]][ny - dy[i]]:  # 이전 위치 방문 안했으면
                            visited[nx - dx[i]][ny - dy[i]] = True  # 이전 위치 방문 체크
                            queue.append([nx - dx[i], ny - dy[i]])  # 이전 위치 큐에 넣기
                            break  # 방문 안했을 때 break
                        break  # 범위 밖일 때 break

                    if board[nx][ny] == "D":  # 다음 위치가 벽이면
                        if not visited[nx - dx[i]][ny - dy[i]]:  # 벽이고, 이전 위치를 방문 안했으면
                            visited[nx - dx[i]][ny - dy[i]] = True  # 이전 위치 방문 체크
                            queue.append([nx - dx[i], ny - dy[i]])  # 이전 위치 큐에 넣기
                            break  # 방문 안했을 때 break
                        break  # 벽 일때 break
                    # 중요!! 위치와 방문 체크를 and로 함께 하면, 방문 안한 벽이거나, 범위 밖이여서 잘못된 값이 들어감!
                    # 따라서 따로따로 체크 해야함!
                    # 예시로 다음이 벽이면 무조건 멈춰야하지만, 이전 위치가 방문 안했으면, while문을 타서 계속 돔! => 오류
        if flag:  # 위치 찾았다면
            break  # 끝
        answer += 1  # 시간 + 1

    if not flag:  # 위치 못찾았으면
        answer = -1  # -1

    return answer