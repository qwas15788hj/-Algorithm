from collections import deque

t = int(input())
for _ in range(t):
    count = 0
    n, m = map(int, input().split())
    queue = deque([])
    a = list(map(int, input().split()))
    for i in a:
        queue.append([i, 0])
    queue[m][1] = 1

    while True:
        for i in range(1, len(queue)):
            if queue[0][0] < queue[i][0]:
                queue.append(queue.popleft())
                break
        else:
            out = queue.popleft()
            count += 1
            if out[1] == 1:
                print(count)
                break