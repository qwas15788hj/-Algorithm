import sys
input = sys.stdin.readline

t = int(input()) # 테스트케이스 t 입력
for _ in range(t): # 테스트케이스 반복
    m, n, x, y = map(int, input().split()) # m, n, x, y 입력

    k = x # 시작 k 는 x로 고정
    flag = False # 정답 추출 여부
    while k <= m*n: # k가 m*n 까지 돌면서
        if (k-x)%m == 0 and (k-y)%n == 0: # 시작점 k-x를 m으로 나눈것과 k-y를 n으로 나눈것이 떨어지면 정답
            print(k)
            flag = True
            break
        k += m # 시작점 k는 x이므로 m으로 나눈 것의 나머지여야함으로 m 더해주기

    if not flag:
        print(-1)