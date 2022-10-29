'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/10/06
boj.kr/1976
여행 가자
'''
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())

cities = [[] for _ in range(N)]

# 도시들간 도로 구성
for i in range(N):
    road = list(map(int, input().split()))
    for j in range(len(road)):
        if road[j] == 1:
            cities[i].append(j)
            cities[j].append(i)
plan = list(map(int, input().split()))
# check another circle
all_visited = [0 for _ in range(N)]
can = True
while(0 in all_visited):
    # plan 에 없는 도시를 찾아서 이를 제외한 스패닝 트리를 찾아야함.
    visited = [0 for _ in range(N)]
    
    city_queue = deque()
    for i in range(len(all_visited)):
        if all_visited[i] == 0:
            city_queue.append(i)
            break

    while(city_queue):
        now_city = city_queue.popleft()

        if visited[now_city] == 1:
            continue
        else :
            visited[now_city] = 1
            for city in cities[now_city]:
                if visited[city] == 0:
                    city_queue.append(city)

    can = True
    for city in plan:
        if visited[city-1] != 1:
            can = False
            break

    if can:
        print("YES")
        break
    
    for i in range(len(visited)):
        all_visited[i] += visited[i]

    
if not can:
    print("NO")