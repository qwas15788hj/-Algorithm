n, b = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
start = 0
end = 2000000000

while start <= end:
    mid = (start+end)//2
    cost = 0
    for i in arr:
        if mid > i:
            cost += (mid-i)**2
    if cost > b:
        end = mid-1
    else:
        start = mid+1
        answer = mid

print(answer)