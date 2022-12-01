from collections import deque

def bfs(x, visited, network):
    queue = deque()
    queue.append(x)
    count = 1
    visited[x] = True
    while queue:
        nx = queue.popleft()
        size = len(network[nx]) # 현재 정점과 연결된 정점 개수만큼
        for i in range(size):
            if(not visited[network[nx][i]]): # 현재 정점과 연결된 정점이 방문안했다면
                queue.append(network[nx][i])
                visited[network[nx][i]] = True
                count += 1
                
    return count
        

def solution(n, wires):
    answer = 1e9
    # 네트워크 연결 정보
    networks = [[]*(n+1) for _ in range(n+1)]
    for i in range(len(wires)):
        networks[wires[i][0]].append(wires[i][1])
        networks[wires[i][1]].append(wires[i][0])
        
    # 연결선 하나씩 제거
    for i in range(len(wires)):
        network = [i[:] for i in networks]
        a = wires[i][0]
        b = wires[i][1]
        for j in range(len(network[a])):
            if network[a][j]==b:
                network[a].pop(j)
                break
        for j in range(len(network[b])):
            if network[b][j]==a:
                network[b].pop(j)
                break
        ## 제거 완료
        
        # 제거한 정점 a, b 각각 bfs돌려 연결 지점 찾기
        visited = [False]*(n+1)
        a_cnt = bfs(a, visited, network)
        visited = [False]*(n+1)
        b_cnt = bfs(b, visited, network)
        
        answer = min(answer, abs(a_cnt-b_cnt))
    
    return answer