n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
target = list(map(int, input().split()))

for num in target:
    start = 0
    end = n-1
    flag = False
    while start <= end:
        mid = (start+end)//2
        if num == arr[mid]:
            print(1)
            flag = True
            break
        elif num < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    if not flag:
        print(0)