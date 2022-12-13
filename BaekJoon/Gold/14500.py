import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split()))) #입력

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] #4방면

def dfs(x, y, cnt, score): #ㅗ, ㅓ, ㅏ, ㅜ 모양 빼고 나머지
    global answer
    if cnt==4: #4면 다 찾았다면
        answer = max(answer, score) #정답 갱신
        return
    for i in range(4): #4방면 돌면서
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]: #범위에 있고 방문 안했다면
            visited[nx][ny] = True #방문 체크
            dfs(nx, ny, cnt+1, score+arr[nx][ny]) #dfs돌기
            visited[nx][ny] = False #다 돌았다면 False

def bfs(x, y): #ㅗ, ㅓ, ㅏ, ㅜ 모양 체크
    global answer
    for i in range(4): #4번 체크!
        score = arr[x][y] #기준점 점수
        for j in range(4): #4방향 보면서
            if i != j: #현재 체크하는 방향이랑 다른 방향만!
                nx = x+dx[j]
                ny = y+dy[j]
                if 0<=nx<n and 0<=ny<m: #범위에 있다면
                    score += arr[nx][ny] #점수 추가
                else: #범위에 벗어나면
                    break #멈추기
        answer = max(answer, score)

answer = 0
visited = [[False]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        visited[i][j] = True #방문완료
        dfs(i, j, 1, arr[i][j]) #dfs 호출
        visited[i][j] = False #방문해제 (다음 위치에서의 dfs 위해서)
        bfs(i, j)

print(answer)