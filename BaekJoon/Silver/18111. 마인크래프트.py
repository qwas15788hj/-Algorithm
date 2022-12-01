import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

answer = 1e9
height = 0
for k in range(257):
    remove = 0
    put = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] > k:
                remove += arr[i][j]-k
            else:
                put += k-arr[i][j]

    if put > remove+b:
        continue

    time = remove*2 + put
    if answer > time:
        answer = time
        height = k
    elif answer == time:
        height = max(height, k)

print(answer, height)