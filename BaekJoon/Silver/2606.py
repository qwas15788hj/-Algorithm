from collections import deque

n = int(input())
m = int(input())
network = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

def bfs(start):
    queue = deque([])
    queue.append(start)
    visited = [False]*(n+1)
    count = 1
    visited[start] = True
    while queue:
        x = queue.popleft()
        for i in network[x]:
            if not visited[i]:
                count += 1
                visited[i] = True
                queue.append(i)
    return count

print(bfs(1)-1)