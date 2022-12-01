n = int(input())
arr = list(map(int, input().split()))
arr.sort()
time = 0
for i in range(1, n+1):
    time += sum(arr[:i])
print(time)