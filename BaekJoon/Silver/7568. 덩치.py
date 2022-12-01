n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

answer = []
for i in range(n):
    cnt = 1
    for j in range(n):
        if i==j:
            continue
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt += 1
    answer.append(cnt)

for i in answer:
    print(i, end=" ")