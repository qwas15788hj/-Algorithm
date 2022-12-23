n = int(input())
s = str(n)

answer = 0
answer += ((n-10**(len(s)-1)+1)*len(s))%1234567
for i in range(len(s)-1, 0, -1):
    answer += (9*(10**(i-1)))%1234567

print(answer%1234567)