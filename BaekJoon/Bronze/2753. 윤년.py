n = int(input())
answer = 0
if n%4==0 and n%100!=0:
    answer = 1
elif n%100==0 and n%400!=0:
    answer = 0
elif n%400==0:
    answer = 1
print(answer)