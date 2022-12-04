n = int(input())
arr = list(map(int, input().split()))

stack = []
count = 0
for i in range(len(arr)-2):
    stack.append(arr[i])
    for j in range(i+1, len(arr)-1):
        stack.append(arr[j])
        for z in range(j+1, len(arr)):
            stack.append(arr[z])
            if stack[0] < stack[1] and stack[0] > stack[2]:
                count += 1
            stack.pop()
        stack.pop()
    stack.pop()

print(count)