from collections import deque


def solution(x, y, n):
    answer = 0

    queue = deque()
    visited = [False] * 1000001

    queue.append(x)
    visited[x] = True

    flag = False
    while queue:
        size = len(queue)
        for _ in range(size):
            num = queue.popleft()
            if num == y:
                flag = True
                break
            if num + n < 1000001 and x + n <= y and not visited[num + n]:
                queue.append(num + n)
                visited[num + n] = True
            if num * 2 < 1000001 and num * 2 <= y and not visited[num * 2]:
                queue.append(num * 2)
                visited[num * 2] = True
            if num * 3 < 1000001 and num * 3 <= y and not visited[num * 3]:
                queue.append(num * 3)
                visited[num * 3] = True

        if flag:
            break

        answer += 1

    if not flag:
        answer = -1

    return answer
