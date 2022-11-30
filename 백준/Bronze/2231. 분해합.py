n = int(input())
num = 0
while True:
    sum = num
    for i in str(num):
        sum += int(i)
    if sum == n:
        print(num)
        break
    if num > n:
        print(0)
        break
    num += 1