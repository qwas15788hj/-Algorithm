answer = 1e9

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(input())

for i in range(n-8+1): #세로
    for j in range(m-8+1): #가로
        start = arr[i][j]
        count = 0
        for z in range(i, i+8):
            for p in range(j, j+8):
                if (z+p-(i+j))%2==0:
                    if arr[z][p] != start:
                        count += 1
                else:
                    if arr[z][p] == start:
                        count += 1
        answer = min(answer, count, 64-count)

print(answer)