n = int(input()) # n개 입력
money = [0] + list(map(int, input().split())) # 카드 값 입력
card = [1e9]*(1001) # 카드 총 개수를 최대값으로 채운 배열
card[0] = 0 # 카드 0은 0원

for i in range(n+1): # 뽑아야하는 n카드까지 돌면서
    for j in range(i+1): # 현재 카드와 같은 개수의 카드돈까지 확인
        card[i] = min(card[i], money[j]+card[i-j]) # 현재 카드 값= 현재카드와 이전 카드의 돈+그때까지의 카드 값

print(card[n]) # n번째 카드 뽑을때 값 출력