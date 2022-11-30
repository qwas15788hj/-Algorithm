from collections import deque

def bfs(x):
    queue = deque([])
    queue.append(x)
    while queue:
        nx = queue.popleft()
        if nx==k:
            break
        if 0<=nx-1<100001 and arr[nx-1]==0:
            arr[nx-1] = arr[nx]+1
            queue.append(nx-1)
        if 0<=nx+1<100001 and arr[nx+1]==0:
            arr[nx+1] = arr[nx]+1
            queue.append(nx+1)
        if 0<=nx*2<100001 and arr[nx*2]==0:
            arr[nx*2] = arr[nx]+1
            queue.append(nx*2)

n, k = map(int, input().split())
arr = [0]*(100001)
arr[n] = 1
bfs(n)

print(arr[k]-1)