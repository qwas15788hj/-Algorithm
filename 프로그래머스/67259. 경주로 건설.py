from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] #상하좌우

def bfs(board, d):
    queue = deque([])
    queue.append([0, 0, 0, d])
    n = len(board)
    arr = [[1e9]*n for _ in range(n)] #가격 넣을 배열
    arr[0][0] = 0
    
    while queue:
        x, y, c, d = queue.popleft()
        # print("==")
        # print(x, y, c, d)
        for i in range(4): #4방향 돌면서
            nx = x+dx[i]
            ny = y+dy[i]
            nd = i
            if nx<0 or nx>=n or ny<0 or ny>=n: #범위 밖 무시
                continue
            if board[nx][ny]==1: #벽 무시
                continue

            if nd==d: #현재 가는 방향과 같은 방향
                nc = c+100 #이전 가격에 +100
            else:
                nc = c+600

            if nc <= arr[nx][ny]: #방문했던 곳이라도 가격이 싸거나 같으면 추가
                arr[nx][ny] = nc
                # print(nx, ny, nc, nd)
                queue.append([nx, ny, nc, nd])
    
    global answer
    answer = min(answer, arr[n-1][n-1])
                
def solution(board):
    global answer
    answer = 1e9
    
    bfs(board, 3)
    bfs(board, 1)
    
    return answer