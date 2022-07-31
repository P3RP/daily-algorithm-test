'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/07/31
boj.kr/3085
사탕게임

문제 :
상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.

가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다. 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 
그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.

사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.

입력 :
첫째 줄에 보드의 크기 N이 주어진다. (3 ≤ N ≤ 50)
다음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다. 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.
사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.

결과 :
첫째 줄에 상근이가 먹을 수 있는 사탕의 최대 개수를 출력한다.
'''

# 움직이는 것 확인은 오른쪽, 아래만 확인해보면 된다.
# 왜냐하면 위, 왼쪽은 이전것에서 이미 확인하기 때문이다.

import sys
input = sys.stdin.readline

N = int(input())

canndy_list = []

for i in range(N):
    canndy_list.append(list(input().strip()))

def check_row(start, canndy_list):
    (start_row, start_col) = start
    # left
    count = 1
    left_i = start_col - 1
    while(left_i >= 0):
        if canndy_list[start_row][left_i] == canndy_list[start_row][start_col]:
            count += 1
        else :
            break
        left_i -= 1
    
    #right
    right_i = start_col + 1
    while(right_i <len(canndy_list)):
        if (canndy_list[start_row][right_i] == canndy_list[start_row][start_col]):
            count += 1
        else :
            break
        right_i += 1
    return count 

def check_col(start, canndy_list):
    (start_row, start_col) = start
    # up
    count = 1
    up_i = start_row - 1
    while(up_i >= 0):
        if canndy_list[up_i][start_col] == canndy_list[start_row][start_col]:
            count += 1
        else :
            break
        up_i -= 1
    
    # down
    down_i = start_row + 1
    while(down_i <len(canndy_list)):
        if (canndy_list[down_i][start_col] == canndy_list[start_row][start_col]):
            count += 1
        else :
            break
        down_i += 1
    return count 

result = 0
for i in range(N):
    for j in range(N):
        # change right
        now_item = canndy_list[i][j]
        if j+1 < N:
            canndy_list[i][j] = canndy_list[i][j+1]
            canndy_list[i][j+1] = now_item 
            result = max ( result, check_row((i,j), canndy_list))
            result = max ( result, check_row((i,j+1), canndy_list))
            result = max ( result, check_col((i,j), canndy_list))
            result = max ( result, check_col((i,j+1), canndy_list))
            canndy_list[i][j+1] = canndy_list[i][j]
            canndy_list[i][j] = now_item

        # change down
        if i+1 < N:
            canndy_list[i][j] = canndy_list[i+1][j]
            canndy_list[i+1][j] = now_item 
            result = max ( result, check_row((i,j), canndy_list))
            result = max ( result, check_col((i+1,j), canndy_list))
            result = max ( result, check_row((i+1,j), canndy_list))
            result = max ( result, check_col((i,j), canndy_list))
            canndy_list[i+1][j] = canndy_list[i][j]
            canndy_list[i][j] = now_item

print(result)