from collections import Counter
s = input()
arr = s.upper()
val = Counter(arr).most_common()
answer = []
for i in val:
    if i[1] == val[0][1]:
        answer.append(i[0])

if len(answer) > 1:
    print("?")
else:
    print(answer[0])