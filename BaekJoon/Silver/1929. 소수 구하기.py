n, m = map(int, input().split())

for i in range(n, m+1):
    if i==1:
        continue
    else:
        flag = True
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                flag = False
                break
        if flag:
            print(i)