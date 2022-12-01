n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr = arr[::-1]

count = 0
for i in range(n):
    count += k//arr[i]
    k %= arr[i]

print(count)