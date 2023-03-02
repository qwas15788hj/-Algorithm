n = int(input())

size = len(str(n))
answer = 0
for i in range(1, size):
    answer += (9 * pow(10, i-1) * i)%1234567
answer += (size * ((n+1) - pow(10, size-1)))%1234567

print(answer%1234567)