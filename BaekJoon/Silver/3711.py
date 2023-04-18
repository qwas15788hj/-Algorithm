n = int(input())
for _ in range(n):
    g = int(input())
    student = []
    for _ in range(g):
        student.append(int(input()))

    m = 1
    while True:
        arr = []
        for i in range(g):
            arr.append(student[i]%m)
        if len(list(set(arr))) == g:
            print(m)
            break
        m += 1