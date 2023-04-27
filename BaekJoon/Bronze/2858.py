r, b = map(int, input().split())

flag = False
for i in range(3, 5000):
    for j in range(3, 5000):
        if (i*j == r+b) and ((i-2)*(j-2) == b):
            print(j, i)
            flag = True
            break
    if flag:
        break