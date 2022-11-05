from itertools import permutations

def solution(babbling):
    answer = 0
    
    arr = ["aya", "ye", "woo", "ma"]
    word_perm = []
    for i in range(2, 5):
        perm = list(permutations(arr, i))
        for p in perm:
            word_perm.append(p)
    
    for words in word_perm:
        w = ""
        for word in words:
            w += word
        arr.append(w)
    
    for bab in babbling:
        if bab in arr:
            answer += 1
            
    return answer