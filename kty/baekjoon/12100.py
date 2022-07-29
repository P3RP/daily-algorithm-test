'''
******* 문제 푼 후 느낀 것 *********
move 함수에서 deepcopy 로 2차원 배열을 복사하여 넘겨주지 않으니, 배열 값이 변경되어 문제가 풀리지 않았다.
dfs 에서 해당 탐색을 하다 뒤로 돌아오면, 해당 배열의 값이 변경되지 않은 상태이어야 하는데, 
파라미터로 배열을 넘겨주었을때 해당 함수 안에서 배열의 값이 변경되게 되고, 해당 배열은 복사된 배열이 아닌, 원본이기 떄문에
원본이 다시 돌아오지 못하는 문제가 발생한다. 따라서, deepcopy 를 통해 원래 배열을 유지할 수 있도록 해야한다.

백트래킹에서 visited 를 deepcopy 해서 넘기거나, 
visiteid[i] = 1을 해주고, dfs 재귀 이후 visited[i] = 0 으로 다시 변경해주는 방법이 
결과과적으로 동일한 것처럼!
'''

'''
2022/07/29
boj.kr/12100
2048 (Easy)

문제 :
그림이 너무 많은 관계로 생략
'''
import sys
from copy import deepcopy
input = sys.stdin.readline

N = int(input())

board = []

for i in range(N):
    board.append(list(map(int, input().split())))

def move(direction, board):
    # up
    if direction == 0:
        for i in range(N):
            for j in range(N-1):
                if board[j][i] == 0:
                    is_last_zero = True
                    for k in range(j+1, N):
                        if board[k][i] != 0 :
                            board[j][i] = board[k][i]
                            board[k][i] = 0
                            is_last_zero = False
                            break
                    if is_last_zero :
                        break

            for j in range(N-1):
                if board[j][i] == board[j+1][i]:
                    board[j][i] *= 2
                    board[j+1][i] = 0
            
            for j in range(N-1):
                if board[j][i] == 0:
                    is_last_zero = True
                    for k in range(j+1, N):
                        if board[k][i] != 0 :
                            board[j][i] = board[k][i]
                            board[k][i] = 0
                            is_last_zero = False
                            break
                    if is_last_zero :
                        break
    # down
    if direction == 1:
        for i in range(N):
            for j in range(N-1, 0, -1):
                if board[j][i] == 0:
                    is_last_zero = True
                    for k in range(j-1, -1, -1):
                        if board[k][i] != 0 :
                            board[j][i] = board[k][i]
                            board[k][i] = 0
                            is_last_zero = False
                            break
                    if is_last_zero :
                        break
            for j in range(N-1, 0, -1):
                if board[j][i] == board[j-1][i]:
                    board[j][i] *= 2
                    board[j-1][i] = 0
            for j in range(N-1, 0, -1):
                if board[j][i] == 0:
                    is_last_zero = True
                    for k in range(j-1, -1, -1):
                        if board[k][i] != 0 :
                            board[j][i] = board[k][i]
                            board[k][i] = 0
                            is_last_zero = False
                            break
                    if is_last_zero :
                        break

    # left
    if direction == 2:
        for j in range(N):
            for i in range(N-1):
                if board[j][i] == 0:
                    is_last_zero = True
                    for k in range(i+1, N):
                        if board[j][k] != 0 :
                            board[j][i] = board[j][k]
                            board[j][k] = 0
                            is_last_zero = False
                            break
                    if is_last_zero :
                        break
            for i in range(N-1):
                if board[j][i] == board[j][i+1]:
                    board[j][i] *= 2
                    board[j][i+1] = 0
            for i in range(N-1):
                if board[j][i] == 0:
                    is_last_zero = True
                    for k in range(i+1, N):
                        if board[j][k] != 0 :
                            board[j][i] = board[j][k]
                            board[j][k] = 0
                            is_last_zero = False
                            break
                    if is_last_zero :
                        break
    # right:
    if direction == 3:
        for j in range(N):
            for i in range(N-1, 0, -1):
                if board[j][i] == 0:
                    is_last_zero = True
                    for k in range(i-1, -1, -1):
                        if board[j][k] != 0 :
                            board[j][i] = board[j][k]
                            board[j][k] = 0
                            is_last_zero = False
                            break
                    if is_last_zero :
                        break
            for i in range(N-1, 0, -1):
                if board[j][i] == board[j][i-1]:
                    board[j][i] *= 2
                    board[j][i-1] = 0
            for i in range(N-1, 0, -1):
                if board[j][i] == 0:
                    is_last_zero = True
                    for k in range(i-1, -1, -1):
                        if board[j][k] != 0 :
                            board[j][i] = board[j][k]
                            board[j][k] = 0
                            is_last_zero = False
                            break
                    if is_last_zero :
                        break
    return board

def dfs(board, count=0) :
    global max_value
    if count == 5:
        max_value = max(max_value, max(map(max, board)))
        return
    else :        
        for i in range(4):
            dfs(board=move(i,deepcopy(board)), count=count+1)


max_value = 0

dfs(board, 0)
print(max_value)