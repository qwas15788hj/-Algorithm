chess = [1, 1, 2, 2, 2, 8]
arr = list(map(int, input().split()))
for i in range(len(arr)):
    print(chess[i]-arr[i], end=" ")