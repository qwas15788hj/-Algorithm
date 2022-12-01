n, m = map(int, input().split())
person = dict()
for _ in range(n):
    s = input()
    person[s] = 1

answer = []
for _ in range(m):
    s = input()
    if s in person:
        answer.append(s)

answer.sort()
print(len(answer))
for i in answer:
    print(i)