from collections import deque

n = int(input())
arr = []
for i in range(n):
    s = input()
    arrSub = []
    for j in range(len(s)):
        arrSub.append(s[j])
    arr.append(arrSub)

answer = 0
for i in range(n): # n 명
    queue = deque()
    visited = [False] * n
    queue.append(i)
    visited[i] = True
    count = 0
    for j in range(2): # 2-친구까지
        size = len(queue)
        for z in range(size):
            person = queue.popleft() # 현재친구 or 나
            for p in range(len(arr[person])):
                if arr[person][p] == "Y" and not visited[p]:
                    count += 1
                    visited[p] = True
                    queue.append(p)

    answer = max(answer, count)

print(answer)