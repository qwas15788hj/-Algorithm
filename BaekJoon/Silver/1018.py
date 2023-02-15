n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(input())

answer = 1e9
for i in range(n-8+1):
    for j in range(m-8+1):
        start = arr[i][j]
        count = 0
        for z in range(i, i+8):
            for w in range(j, j+8):
                if (z+w-(i+j))%2 == 0:
                    if arr[z][w] != start:
                        count += 1
                else:
                    if arr[z][w] == start:
                        count += 1
        answer = min(answer, count, 64-count)

print(answer)