from collections import Counter

def solution(k, tangerine):
    answer = 0

    arr = Counter(tangerine).most_common()
    for i in arr:
        k -= i[1]
        answer += 1
        if k <= 0:
            break

    return answer