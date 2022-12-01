arr = list(map(int, input().split()))

flag = True
if arr[0]==1:
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]+1:
            flag = False
            print("mixed")
            break
    if flag:
        print("ascending")
elif arr[0]:
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]-1:
            flag = False
            print("mixed")
            break
    if flag:
        print("descending")
else:
    print("mixed")