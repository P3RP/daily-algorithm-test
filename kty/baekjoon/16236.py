'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/08/21
boj.kr/16236
아긔 상어

문제 :
N×N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 물고기가 최대 1마리 존재한다.

아기 상어와 물고기는 모두 크기를 가지고 있고, 이 크기는 자연수이다. 가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.

아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다. 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.

아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.

더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다. 즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다. 물고기를 먹으면, 그 칸은 빈 칸이 된다.

아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.

공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램을 작성하시오.

입력 :
첫째 줄에 공간의 크기 N(2 ≤ N ≤ 20)이 주어진다.

둘째 줄부터 N개의 줄에 공간의 상태가 주어진다. 공간의 상태는 0, 1, 2, 3, 4, 5, 6, 9로 이루어져 있고, 아래와 같은 의미를 가진다.

0: 빈 칸
1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
9: 아기 상어의 위치
아기 상어는 공간에 한 마리 있다.

결과 :
첫째 줄에 아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간을 출력한다.
'''
import sys
from collections import deque
input = sys.stdin.readline

SHARK = 9

N = int(input())
space = [[] for _ in range(N)]

for i in range(N):
    space[i] = list(map(int,input().split()))

# 상어의 위치 (a,b)
# 잡아먹을 물고기의 위치 (c,d) 
# 상대적 거리는 abs(a-c) + abs(b-d)

# 상어 관련 정보
shark_size = 2
shark_eating = 0
# 상어 위치 파악
shark_position = (0,0)
for i in range(N):
    for j in range(N):
        if space[i][j] == SHARK:
            shark_position = (i, j)
            space[i][j] = 0
            break

def eat(x,y):
    global space
    global shark_size
    global shark_eating
    global shark_position
    global shark_time

    if 0 < space[x][y] < shark_size:
        space[x][y] = 0
        shark_eating += 1
        if shark_eating == shark_size:
            shark_size += 1
            shark_eating = 0
        return True
    return False


# 제일 작은 사이즈의 물고기들을 찾는다.
# 반복문? dfs? 
# 문제에서 가장 가까운 거리라 했으므로, bfs를 통해서 찾는것이 좋을 것 같다.
# 그렇다면 현재 위치에서 먹을 수 있는 물고기, 즉 상어보다 크기가 작은 물고기들의 위치를 매번 파악한다.

# deque 가 왼쪽에서 빼내는 것이 빠르므로 deque 를 사용
queue = deque()

# 현재 상어의 위치를 초기 탐색 지점으로 넣어준다
# 이후 이동하면서 먹을 수 있는 물고기를 최초로 발견했다면, queue를 아예 비우고 해당위치에서 다시 시작하도록 해준다
# 이때 이동할 수 있는 지점은 한번에 움직일 수 있는 공간들을 다 queue 에 넣어서 하도록 한다
queue.append(shark_position)



move = [(0,-1), (-1,0), (1,0), (0,1)]
time = 0
shark_time = 0
visited = [[ 0 for _ in range(N)] for _ in range(N)]
visited[shark_position[0]][shark_position[1]] = 1
while(queue):
    max_check = len(queue)
    is_eat = False
    queue = deque(sorted(queue,key=lambda x:[x[0],x[1]]))

    for _ in range(max_check):
        (x,y) = queue.popleft()
        is_eat = eat(x, y)
        if (is_eat):
            queue = deque()
            shark_time = time
            visited = [[ 0 for _ in range(N)] for _ in range(N)]
            visited[x][y] = 1
            
        for (nx,ny) in move:
            if 0 <= x+nx < N and 0 <= y+ny < N and visited[x+nx][y+ny] != 1:
                if space[x+nx][y+ny] <= shark_size:
                    queue.append((x+nx, y+ny))
                    visited[x+nx][y+ny] = 1
        if is_eat:
            break
            
    time += 1
print(shark_time)
