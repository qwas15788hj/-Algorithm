n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x:(x[1], x[0]))
count = 0
finish = 0
for i in range(n):
    if arr[i][0] >= finish:
        finish = arr[i][1]
        count += 1
print(count)