n, m = map(int, input().split())
arr = []
answer = 0
for _ in range(n):
    arr.append(input())

for _ in range(m):
    if input() in arr:
        answer += 1

print(answer)