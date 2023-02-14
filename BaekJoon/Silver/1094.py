x = int(input())
count = 0
for i in range(6, -1, -1):
    if x >= pow(2, i):
        x -= pow(2, i)
        count += 1

print(count)