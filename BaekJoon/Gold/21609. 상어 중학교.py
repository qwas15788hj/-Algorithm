from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def block_group(x, y):
    global block_group_list
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    target = arr[x][y]
    normal_block = 1
    rainbow_block = 0
    rainbow_store = []
    while queue:
        size = len(queue)
        for i in range(size):
            nx, ny = queue.popleft()
            for j in range(4):
                mx = nx + dx[j]
                my = ny + dy[j]
                if (0 <= mx < n and 0 <= my < n and not visited[mx][my] and arr[mx][my] == target):
                    normal_block += 1
                    visited[mx][my] = True
                    queue.append([mx, my])
                if (0 <= mx < n and 0 <= my < n and not visited[mx][my] and arr[mx][my] == 0):
                    rainbow_block += 1
                    visited[mx][my] = True
                    queue.append([mx, my])
                    rainbow_store.append([mx, my])

    for rx, ry in rainbow_store:
        visited[rx][ry] = False
    if (normal_block + rainbow_block >= 2):
        block_group_list.append([x, y, normal_block + rainbow_block, rainbow_block])


def block_remove(x, y):
    queue = deque()
    queue.append([x, y])
    target = arr[x][y]
    arr[x][y] = -2
    while queue:
        size = len(queue)
        for i in range(size):
            nx, ny = queue.popleft()
            for j in range(4):
                mx = nx + dx[j]
                my = ny + dy[j]
                if (0 <= mx < n and 0 <= my < n):
                    if arr[mx][my]==target or arr[mx][my]==0:
                        arr[mx][my] = -2
                        queue.append([mx, my])


def gravity():
    for j in range(n):
        stack = []
        for i in range(n):
            if (arr[i][j] >= 0):
                stack.append(arr[i][j])
                arr[i][j] = -2
            elif (arr[i][j] == -1):
                for k in range(1, len(stack) + 1):
                    arr[i - k][j] = stack.pop()

        if (len(stack) != 0):
            for k in range(len(stack)):
                arr[i - k][j] = stack.pop()


def turn():
    SubArr = [i[:] for i in arr]
    for i in range(n):
        for j in range(n):
            SubArr[i][j] = arr[j][n - 1 - i]

    return SubArr


# 입력
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

answer = 0

while True:
    # 1. 블록 그룹 찾기
    block_group_list = []
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j]>0 and not visited[i][j]:
                block_group(i, j)

    if (len(block_group_list) == 0):
        break
    block_group_list.sort(key=lambda x: (-x[2], -x[3], -x[0], -x[1]))

    # 2. 블록 제거 점수 얻기
    answer += int(block_group_list[0][2] ** 2)
    block_remove(block_group_list[0][0], block_group_list[0][1])

    # 3. 중력
    gravity()

    # 4. 반시계 턴
    arr = turn()

    # 5. 중력
    gravity()

print(answer)