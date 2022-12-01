s = input()
arr = s.split("-")
answer = 0
for i in range(len(arr)):
    a = arr[i].split("+")
    sum = 0
    for j in a:
        sum += int(j)
    if i==0:
        answer += sum
    else:
        answer -= sum
print(answer)