import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

stack = []
op = []
num = 1
cnt = 0
flag = True

while True:
    if num <= arr[cnt]:
        stack.append(num)
        op.append("+")
        num += 1
    elif stack[-1] == arr[cnt]:
        stack.pop()
        op.append("-")
        cnt += 1
    else:
        flag = False
        break
    if cnt==len(arr):
        break

if flag:
    for i in op:
        print(i)
else:
    print("NO")