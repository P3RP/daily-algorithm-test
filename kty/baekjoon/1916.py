'''
******* 문제 푼 후 느낀 것 *********
음수 가중치가 없고, 특정 정점간의 최소거리를 구하는 것은 다익스트라로 푸는 것이 맞다.
Dfs 로 접근하였는데, 시간초과가 발생하였다. 
bfs나 다익스트라를 이용해서 풀어야한다. 다익스트라는 구현이 bfs와 비슷하다
'''

'''
2022/07/22
boj.kr/1963
최소비용 구하기

문제 :
N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다. 
우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. 
A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 도시의 번호는 1부터 N까지이다.

입력 :
첫째 줄에 도시의 개수 N(1 ≤ N ≤ 1,000)이 주어지고 둘째 줄에는 버스의 개수 M(1 ≤ M ≤ 100,000)이 주어진다. 
그리고 셋째 줄부터 M+2줄까지 다음과 같은 버스의 정보가 주어진다. 
먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 

버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.

그리고 M+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다. 출발점에서 도착점을 갈 수 있는 경우만 입력으로 주어진다.

결과 :
첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.
'''

import sys
import heapq
from collections import deque

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end))

start_city, end_city = map(int, input().split())
dist = [sys.maxsize for _ in range(N+1)]

def dijkstra(start):
    dist[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while(heap):
        cur_dist, cur_v = heapq.heappop(heap)
        if cur_dist > dist[cur_v]:
            continue
        for next_dist, next_v in graph[cur_v]:
            new_dist = dist[cur_v] + next_dist
            if new_dist < dist[next_v]:
                dist[next_v] = new_dist
                heapq.heappush(heap, (new_dist, next_v))

dijkstra(start_city)
print(dist[end_city])

'''
bus_way_cost = [{} for _ in range(N+1)]


for _ in range(M):
    start, end, cost = map(int, input().split())
    if end in bus_way_cost[start] :
        bus_way_cost[start][end] = min(cost, bus_way_cost[start][end])
    else :
         bus_way_cost[start][end] = cost

start_city, end_city = map(int, input().split())

visited = [sys.maxsize for _ in range(N+1)]

def bfs(start, visited):
    visited[start] = 0
    q = deque()
    q.append(start)

    while(q):
        v_start = q.popleft()
        for v_end in bus_way_cost[v_start]:
            new_dist = visited[v_start]+ bus_way_cost[v_start][v_end]
            if visited[v_end] > new_dist :
                q.append(v_end)
                visited[v_end] = new_dist

if(start_city == end_city):
    print(0)
else :
    bfs(start_city, visited)
    print(visited[end_city])
'''

'''

min_cost = 100000*1000 + 1

def dfs(now, end, cost_sum=0) :
    global min_cost
    if now == end :
        min_cost = min(min_cost, cost_sum)
        return
    elif(cost_sum > min_cost) :
        return
    else :
        for i in bus_way_cost[now]:
            temp_cost = bus_way_cost[now][i]
            if  temp_cost != 0 :
                bus_way_cost[now][i] = 0
                cost_sum += temp_cost
                dfs(i, end, cost_sum)
                cost_sum -= temp_cost
                bus_way_cost[now][i] = temp_cost

dfs(start_city, end_city)
'''
