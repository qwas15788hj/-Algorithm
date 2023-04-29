from collections import deque

n, k = map(int, input().split())

visited = [False]*100001
time = [0]*100001
queue = deque()
visited[n] = True
queue.append(n)

while queue:
    x = queue.popleft()
    if 0 <= x-1 <= 100000:
        if not visited[x-1]: # 방문 안했다면
            visited[x-1] = True # 방문 체크
            time[x-1] = time[x] + 1 # 시간 +1
            queue.append(x-1) # 다음 이동 칸 넣기
        else: # 방문 했다면
            time[x-1] = min(time[x-1], time[x] + 1) # 둘 중 시간 작은 걸로

    if 0 <= x+1 <= 100000:
        if not visited[x+1]:
            visited[x+1] = True
            time[x+1] = time[x] + 1
            queue.append(x+1)
        else:
            time[x+1] = min(time[x+1], time[x] + 1)

    if 0 <= x*2 <= 100000:
        if not visited[x*2]:
            visited[x*2] = True
            time[x*2] = time[x]
            queue.append(x*2)
        else:
            time[x*2] = min(time[x*2], time[x])

print(time[k])