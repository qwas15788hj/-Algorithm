n, m = map(int, input().split())
j = int(input())

count = 0
now = 1
for _ in range(j):
    apple = int(input())
    if apple > now + m - 1:
        count += apple - (now + m -1)
        now = apple - m + 1
    elif apple < now:
        count += now - apple
        now = apple

print(count)