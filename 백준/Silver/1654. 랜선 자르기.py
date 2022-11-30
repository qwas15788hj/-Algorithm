k, n = map(int, input().split())
arr = []
for _ in range(k):
    arr.append(int(input()))

start = 1
end = max(arr)
answer = 0
while start <= end:
    count = 0
    mid = (start+end)//2
    for i in range(len(arr)):
        if arr[i] >= mid:
            count += arr[i]//mid

    if count < n:
        end = mid-1
    else:
        start = mid+1
        answer = mid

print(answer)