from collections import deque

def solution(tickets):
    answer = []
    tickets.sort(key=lambda x:(x[1]))
    travel = dict()
    for start, end in tickets:
        if(start in travel.keys()):
            travel[start].append(end)
        else:
            travel[start] = [end]
            
    queue = deque()
    queue.append("ICN")
                 
    while(queue):
        start = queue[-1]

        if start not in travel.keys() or len(travel[start])==0:
            answer.append(queue.pop())
        else:
            queue.append(travel[start][0])
            del travel[start][0]

        # print(queue)
        # print(travel)
    answer.reverse()
    return answer