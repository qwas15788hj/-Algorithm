n = int(input())
s = input()
answer = 0
for i in range(n):
    answer += (ord(s[i])-96)*pow(31, i)

print(answer//1234567891)