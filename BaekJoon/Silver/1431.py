n = int(input())
arr = []
for _ in range(n):
    arr.append(input())


def sort(s):
    count = 0
    for i in range(len(s)):
        if s[i].isdigit():
            count += int(s[i])
    return count


arr.sort(key=lambda x: (len(x), sort(x), x))
for i in range(len(arr)):
    print(arr[i])