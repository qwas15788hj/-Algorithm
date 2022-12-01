import heapq

def solution(n, works):
    answer = 0
    h = []
    for work in works:
        heapq.heappush(h, (-work, work)) #최대힙
    
    
    for _ in range(n):
        a, b = heapq.heappop(h)
        a+=1
        b-=1
        if b > 0:
            heapq.heappush(h, (a, b))
        if len(h)==0:
            break
    
    for i in range(len(h)):
        answer += h[i][0]**2
    
    return answer