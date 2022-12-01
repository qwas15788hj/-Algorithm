from collections import deque

def dfs(start):
    visited[start] = True
    print(start, end=" ")
    for i in arr[start]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    queue = deque([])
    queue.append(start)
    visited[start] = True
    while queue:
        x = queue.popleft()
        print(x, end=" ")
        for i in arr[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
for i in arr:
    i.sort()

visited = [False]*(n+1)
dfs(v)
print()
visited = [False]*(n+1)
bfs(v)