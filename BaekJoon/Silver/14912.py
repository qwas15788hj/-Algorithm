n, d = map(int, input().split())
answer = 0
for i in range(1, n+1):
    for j in range(len(str(i))):
        if int(str(i)[j]) == d:
            answer += 1

print(answer)