from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        x = queue.popleft()
        for i in range(n):
            if(arr[x][i]==1 and not visited[i]):
                queue.append(i)
                visited[i] = True
                result[start][i] = 1


n = int(input())
arr = []
result = [[0]*n for _ in range(n)]
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    visited = [False]*n
    bfs(i)

for i in range(len(result)):
    print(*result[i])