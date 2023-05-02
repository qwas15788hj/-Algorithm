n = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = arr[len(arr)//2]
if len(arr)%2 == 0:
    idx1 = len(arr)//2 - 1
    idx2 = len(arr)//2
    cnt1 = 0
    cnt2 = 0
    for i in range(len(arr)):
        cnt1 += abs(arr[i] - arr[idx1])
        cnt2 += abs(arr[i] - arr[idx2])
    if cnt1 > cnt2:
        answer = arr[idx2]
    else:
        answer = arr[idx1]

print(answer)