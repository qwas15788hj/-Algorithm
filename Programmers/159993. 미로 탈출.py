from collections import deque

def solution(maps):
    answer = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(maps)
    m = len(maps[0])
    lever_queue = deque()
    visited = [[0] * m for _ in range(n)]
    st_flag = False

    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                lever_queue.append([i, j])
                visited[i][j] = 1
                st_flag = True
                break
        if st_flag:
            break

    lever_flag = False
    start_x = 0
    start_y = 0
    while lever_queue:
        x, y = lever_queue.popleft()
        if maps[x][y] == "L":
            answer += visited[x][y] - 1
            start_x = x
            start_y = y
            lever_flag = True
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and maps[nx][ny] != "X":
                lever_queue.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

    end_queue = deque()
    visited = [[0] * m for _ in range(n)]
    end_queue.append([start_x, start_y])
    visited[start_x][start_y] = 1
    end_flag = False
    if lever_flag:
        while end_queue:
            x, y = end_queue.popleft()
            if maps[x][y] == "E":
                answer += visited[x][y] - 1
                end_flag = True
                break
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and maps[nx][ny] != "X":
                    end_queue.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1

    if not lever_flag or not end_flag:
        answer = -1

    return answer