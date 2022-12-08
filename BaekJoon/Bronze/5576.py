w = []
k = []
for _ in range(10):
    w.append(int(input()))
for _ in range(10):
    k.append(int(input()))

w.sort(reverse=True)
k.sort(reverse=True)
print(w[0]+w[1]+w[2], end=" ")
print(k[0]+k[1]+k[2])