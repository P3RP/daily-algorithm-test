import heapq
def solution(scoville, K):
    answer = 0
    
    hq = heapq.heapify(scoville)
    print(hq)
    while(hq[0] < K):
        if len(hq) < 2:
            return -1
        item1 = heapq.heappop(scoville)
        item2 = heapq.heappop(scoville)
        heapq.heappush(hq, item1+(item2*2))
        answer += 1
        
    return answer

print(solution([1,1], 3))