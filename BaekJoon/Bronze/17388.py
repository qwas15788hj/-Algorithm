arr = list(map(int, input().split()))

if sum(arr) >= 100:
    print("OK")
else:
    idx = arr.index(min(arr))
    if idx == 0:
        print("Soongsil")
    elif idx == 1:
        print("Korea")
    else:
        print("Hanyang")