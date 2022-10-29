'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/10/26
boj.kr/17484
진우의 달 여행(small)
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

move_list = [(1,0), (1,-1), (1,1)]

road = []

for _ in range(N):
    road.append(list(map(int, input().split())))


min_cost = sys.maxsize

def dfs(start, before_move, cost):
    global min_cost
    if cost >= min_cost:
        return
        
    if start[0] == N-1:
        min_cost = min(cost, min_cost)
    
    now_x , now_y = start
    for x,y in move_list:
        if x == before_move[0] and y == before_move[1]:
            continue

        next_x = now_x + x
        next_y = now_y + y
        if 0 <= next_x < N and 0 <= next_y < M:
            new_cost = cost + road[next_x][next_y]
            dfs((next_x, next_y), (x,y), new_cost)



for i in range(M):
    dfs((0,i), (0,0), road[0][i])

print(min_cost)