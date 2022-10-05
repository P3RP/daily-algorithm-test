'''
******* 문제 푼 후 느낀 것 *********
heapq를 이용하면 느리다. deque를 쓰는것이 훨씬 바르다.
heapq는 트리구조를 유지해야하기 때문에 시간이 오래 걸리는 것 같다.

또한 이런 최단거리 문제에서는 다익스트라가 별로 좋지 않은 것 같다.
다익스트라는 가중 그래프의 경우에서 효과적이다. 

가중치가 없거나, 모든 가중치가 동일한 경우에서는 BFS를 이용하여 구하는 것이 가장 빠르다.

최단거리가 나왔다고 무조건 다익스트라를 사용하는 것이 아니라는 것 꼭 명심하고 문제를 풀도록 하자.

또한 여기서 벽을 뚫었는지 안뚫었는지 여부를 배열에 넣어서 저장하고 있는데, 이것을 처음 보았을때는 dfs로 
확인해야 하나 싶었다. 하지만 최대 1000*1000 짜리 배열에 대해 dfs를 사용하는 것을 비효율적이라 생각하였고,
어떻게 푸는 것이 좋을지 잘 떠오르지 않아 찾아본 결과 3차원 배열을 사용하여 저장하고 있었다. 
아니면 2차원 배열을 하나 더 만들어서 visited로 놔둬도 괜찮았을 것 같다.

좀 더 고민하고 신중하게 풀 수 있도록 하자.
'''

'''
2022/09/06
boj.kr/2206
벽 부수고 이동하기
'''
import sys
import heapq
from collections import deque

input = sys.stdin.readline

move = [(0,1), (0,-1), (1,0) , (-1,0)]

N, M = map(int, input().split())

load = []
for _ in range(N):
    load.append(input().strip())

shortest = [[[sys.maxsize for _ in range(2)] for _ in range(M)] for _ in range(N)]

shortest[0][0][0] = 1

# distance, x, y
# check_load = []
# heapq.heappush(check_load, (1,0,0,0))

check_load = deque()
check_load.append((1,0,0,0))

value = -1
while(check_load):
    now_dist, now_x, now_y, now_wall = check_load.popleft()
    
    if now_x == N-1 and now_y == M-1:
        value = now_dist
        break

    else :
        for nx,ny in move:
            next_x = now_x + nx
            next_y = now_y + ny
            
            # 벽을 뚫지 않고 가는 경우
            if 0 <= next_x < N and 0 <= next_y < M and load[next_x][next_y] != '1' :
                if shortest[next_x][next_y][now_wall] > now_dist + 1 :
                    shortest[next_x][next_y][now_wall] = now_dist+1
                    # heapq.heappush(check_load, (now_dist+1, next_x, next_y, now_wall))
                    check_load.append((now_dist+1, next_x, next_y, now_wall))
            
            # 벽을 뚫고 가는 경우
            if now_wall == 0:
                if 0 <= next_x < N and 0 <= next_y < M and load[next_x][next_y] == '1' :
                    if shortest[next_x][next_y][1] > now_dist + 1 :
                        shortest[next_x][next_y][1] = now_dist+1
                        # heapq.heappush(check_load, (now_dist+1, next_x, next_y, 1))
                        check_load.append((now_dist+1, next_x, next_y, 1))
    

print(value)