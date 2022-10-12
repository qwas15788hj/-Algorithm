from collections import Counter

def Rcalcu():
    SubArr = [[] for _ in range(len(arr))]
    for i in range(len(arr)):
        zero_list = Counter(arr[i]).most_common()
        list = []
        for zero in zero_list:
            if(zero[0]!=0):
                list.append(zero)
        list.sort(key=lambda x:(x[1], x[0]))
        for li in list:
            SubArr[i].append(li[0])
            SubArr[i].append(li[1])

    l = 0
    for i in range(len(SubArr)):
        l = max(l, len(SubArr[i]))

    for i in range(len(SubArr)):
        if(len(SubArr[i])!=l):
            for _ in range(l-len(SubArr[i])):
                SubArr[i].append(0)

    return SubArr

def op_rotate():
    arr_x = len(arr) #5
    arr_y = len(arr[0]) #3
    SubArr = [[0]*arr_x for _ in range(arr_y)]
    for i in range(arr_y):
        for j in range(arr_x):
            SubArr[i][j] = arr[j][arr_y-1-i]

    return SubArr

def rotate():
    arr_x = len(arr) #5
    arr_y = len(arr[0]) #3
    SubArr = [[0]*arr_x for _ in range(arr_y)]
    for i in range(arr_y):
        for j in range(arr_x):
            SubArr[i][j] = arr[arr_x-1-j][i]

    return SubArr

r, c, k = map(int, input().split())
arr = []
for _ in range(3):
    arr.append(list(map(int, input().split())))

time = 0
while True:
    if(r-1 < len(arr) and c-1 < len(arr[0])):
        if(arr[r-1][c-1]==k):
            print(time)
            break

    if len(arr) >= len(arr[0]):
        arr = Rcalcu()
    else:
        arr = op_rotate()
        arr = Rcalcu()
        arr = rotate()
    time+=1
    if time > 100:
        print(-1)
        break