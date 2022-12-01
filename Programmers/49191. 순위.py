from collections import deque

def bfs(x, arr, visited):
    queue = deque()
    visited[x] = True
    queue.append(x)
    while queue:
        nx = queue.popleft()
        for mx in arr[nx]:
            if not visited[mx]:
                queue.append(mx)
                visited[mx] = True
                global count
                count += 1
    
def solution(n, results):
    answer = 0
    
    arr = [[] for _ in range(n+1)]
    arr_rev = [[] for _ in range(n+1)]
    
    for a, b in results:
        arr[a].append(b)
        arr_rev[b].append(a)
        
    for i in range(1, n+1):
        global count
        count = 0
        visited = [False]*(n+1)
        bfs(i, arr, visited)
        bfs(i, arr_rev, visited)
        if count==n-1:
            answer += 1
    
    return answer