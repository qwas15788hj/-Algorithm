from collections import deque

def bfs(start, visited, graph, answer):
    count = 1
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        size = len(queue)
        for _ in range(size):
            x = queue.popleft()
            for i in range(len(graph[x])):
                if(not visited[graph[x][i]]):
                    queue.append(graph[x][i])
                    visited[graph[x][i]] = True
                    answer[graph[x][i]] = count
        
        count += 1
    
    
def solution(n, edge):
    answer = [0]*(n+1)
    
    graph = [[]*(n+1) for _ in range(n+1)]
    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)
    
    
    visited = [False]*(n+1)
    bfs(1, visited, graph, answer)
    
    cnt = 0
    num = max(answer)
    for i in answer:
        if i==num:
            cnt += 1;
    
    return cnt