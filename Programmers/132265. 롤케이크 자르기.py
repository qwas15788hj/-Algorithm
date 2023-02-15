def solution(topping):
    answer = 0
    a = [0] * 10001
    b = [0] * 10001
    for i in topping:
        b[i] += 1
    a_count = 0
    b_count = len(set(topping))

    for i in range(len(topping)):
        if a[topping[i]] == 0:
            a_count += 1
        a[topping[i]] += 1

        b[topping[i]] -= 1
        if b[topping[i]] == 0:
            b_count -= 1

        if a_count == b_count:
            answer += 1

    return answer