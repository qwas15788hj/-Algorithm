price = 0
arr = []
for _ in range(3):
    arr.append(int(input()))
price += min(arr)

arr = []
for _ in range(2):
    arr.append(int(input()))
price += min(arr)

print(price - 50)