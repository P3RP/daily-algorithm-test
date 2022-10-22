'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/10/22
boj.kr/5972
택배 배송
'''
import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())

paths = [[] for _ in range(N)]

# 우선순위 큐에 넣는다.
# 다익스트라로 풀어야 될듯?
for _ in range(M):
    a, b, value = map(int, input().split())
    paths[a-1].append((value, b-1))
    paths[b-1].append((value, a-1))

path_queue = [(0, (0,0))]
cost = [sys.maxsize for _ in range(N)]
while(path_queue):
    value, (a, b) = heapq.heappop(path_queue)
    # 현재 값이 더 크다면 확인하지 않는다.
    if value > cost[b]:
        continue
    
    for path_cost, next_b in paths[b]:
        # 현재 값이 더 크다면 값을 업데이트하고, 우선순위 큐에 넣어준다
        if cost[next_b] > path_cost + value:
            cost[next_b] = path_cost + value
            heapq.heappush(path_queue, (cost[next_b], (b, next_b)))

print(cost[N-1])