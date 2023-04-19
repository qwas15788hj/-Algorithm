arr = []
for _ in range(5):
    arr.append(list(map(int, input().split())))

num = []
for _ in range(5):
    n = list(map(int, input().split()))
    for i in range(5):
        num.append(n[i])

check = [[0] * 5 for _ in range(5)]


def width(check_arr):
    count = 0
    for i in range(5):
        if sum(check_arr[i]) == 5:
            count += 1
    return count


def length(check_arr):
    count = 0
    for i in range(5):
        cnt = 0
        for j in range(5):
            cnt += check_arr[j][i]
        if cnt == 5:
            count += 1
    return count


def dia(check_arr):
    count = 0
    cnt_x = 0
    cnt_y = 0
    for i in range(5):
        cnt_x += check_arr[i][i]
        cnt_y += check_arr[i][4 - i]
    if cnt_x == 5:
        count += 1
    if cnt_y == 5:
        count += 1
    return count


for i in range(25):
    now = num[i]
    flag = False
    for j in range(5):
        for z in range(5):
            if arr[j][z] == now:
                check[j][z] = 1
                flag = True
                break
        if flag:
            break

    if width(check) + length(check) + dia(check) >= 3:
        print(i + 1)
        break
