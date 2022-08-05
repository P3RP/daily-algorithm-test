'''
******* 문제 푼 후 느낀 것 *********
진짜 개 ㅂㄷㅂㄷ하다.
파이썬은 속도가 느려서 dfs 또는 bfs를 이용해서 풀게되면 시간초과가 발생한다..
따라서 C 언어와 같이 빠른 언어를 사용하거나, DP 를 이용하여 풀어야한다.

그런데 DP 로 푸는 방법은 감조차 오지 않는다...
'''
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

house_map = []
for _ in range(N):
    house_map.append(list(map(int,input().split())))

def move(start, end):
    global house_map
    global N
    (start_x, start_y) = start
    (end_x, end_y, position_type) = end
    # 가로 0, 세로 1, 대각 2
    return_list = []
    

    if position_type == 0:
        if end_y + 1 < N and house_map[end_x][end_y+1] == 0 :
            return_list.append((end_x, end_y+1, 0)) 

        if end_y + 1 < N and end_x + 1 < N:
            if house_map[end_x][end_y+1] == 0 and house_map[end_x+1][end_y] == 0 and house_map[end_x+1][end_y+1] == 0:
                return_list.append((end_x+1, end_y+1, 2))           
    elif position_type == 1:
        if end_x + 1 < N and house_map[end_x+1][end_y] == 0 :
            return_list.append((end_x+1, end_y, 1)) 

        if end_y + 1 < N and end_x + 1 < N:
            if house_map[end_x][end_y+1] == 0 and house_map[end_x+1][end_y] == 0 and house_map[end_x+1][end_y+1] == 0:
                return_list.append((end_x+1, end_y+1, 2))      
    else:
        if end_y + 1 < N and house_map[end_x][end_y+1] == 0 :
            return_list.append((end_x, end_y+1, 0)) 

        if end_x + 1 < N and house_map[end_x+1][end_y] == 0 :
            return_list.append((end_x+1, end_y, 1)) 

        if end_y + 1 < N and end_x + 1 < N:
            if house_map[end_x][end_y+1] == 0 and house_map[end_x+1][end_y] == 0 and house_map[end_x+1][end_y+1] == 0:
                return_list.append((end_x+1, end_y+1, 2))    
    return return_list

def dfs(start, end) :
    global count
    if end[0] == N -1 and end[1] == N - 1:
        count += 1
        return
    else :
        result = move(start, end)
        for item in result :
            dfs((end[0], end[1]), (item[0], item[1], item[2]))
count = 0
dfs((0,0), (0,1,0))
print(count)

'''
queue = deque()
queue.append(((0,0), (0,1)))
count = 0

if house_map[N-1][N-1] == 1 :
    print(count)
else :
    while(queue):
        (start, end) = queue.popleft()
        result = move(start, end)
        for item in result :
            start = end
            new_end = item
            
            (end_x, end_y) = new_end
            if end_x == N-1 and end_y == N-1:
                count += 1
            else :
                queue.append((start, new_end))

    print(count)
'''