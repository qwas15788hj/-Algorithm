t = int(input())
for _ in range(t):
    n = int(input())
    cloth = dict()
    for i in range(n):
        s = list(map(str, input().split()))
        if s[1] in cloth:
            cloth[s[1]].append(s[0])
        else:
            cloth[s[1]] = [s[0]]

    count = 1
    for i in cloth:
        count *= (len(cloth[i])+1)
    print(count-1)