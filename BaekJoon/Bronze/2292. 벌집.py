n = int(input())
house = 1
count = 1
while n > count:
    count += 6*house
    house+=1
print(house)