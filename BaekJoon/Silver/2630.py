n = int(input())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

white = 0
blue = 0

def binary(arr):
    global white, blue
    x = len(arr)
    half = x//2
    total = 0
    for i in range(x):
        total += sum(arr[i])
    if total == 0:
        white += 1
    elif total == x*x:
        blue += 1
    else:
        if x > 1:
            SubArr = [[0]*half for _ in range(half)]
            for i in range(half):
                for j in range(half):
                    SubArr[i][j] = arr[i][j]
            binary(SubArr)
            SubArr = [[0]*half for _ in range(half)]
            for i in range(half):
                for j in range(half):
                    SubArr[i][j] = arr[i+half][j]
            binary(SubArr)
            SubArr = [[0]*half for _ in range(half)]
            for i in range(half):
                for j in range(half):
                    SubArr[i][j] = arr[i][j+half]
            binary(SubArr)
            SubArr = [[0]*half for _ in range(half)]
            for i in range(half):
                for j in range(half):
                    SubArr[i][j] = arr[i+half][j+half]
            binary(SubArr)

binary(paper)
print(white)
print(blue)