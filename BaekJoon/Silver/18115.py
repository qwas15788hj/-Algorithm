from collections import deque

n = int(input())
arr = list(map(int, input().split()))
arr.reverse()

answer = deque()
for i in range(n):
    if arr[i] == 1:
        answer.appendleft(i+1)
    elif arr[i] == 2:
        answer.insert(1, i+1)
    else:
        answer.append(i+1)

print(*answer)