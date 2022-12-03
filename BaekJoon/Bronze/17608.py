import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

stack = []
stack.append(arr[-1])
count = 1
for i in range(n-1, -1, -1):
    if arr[i] > stack[-1]:
        stack.append(arr[i])
        count += 1

print(count)