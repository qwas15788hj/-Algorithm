from bisect import  bisect_left, bisect_right

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr_2 = list(map(int, input().split()))

arr.sort()
for i in range(m):
    left = bisect_left(arr, arr_2[i])
    right = bisect_right(arr, arr_2[i])
    print(right-left, end=" ")