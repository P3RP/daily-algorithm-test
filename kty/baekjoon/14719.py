'''
******* 문제 푼 후 느낀 것 *********
더 쉬운 방법이 존재한다.
매 칸을 검사하면서, 자기 자신 기준으로 max값을 구해서 하는 방법이 존재한다.
-> 이러한 방법도 빠르게 고안할 수 있도록 뇌를 기르자!
'''

'''
2022/07/18
boj.kr/14719
빗물

문제 :
2차원 세계에 블록이 쌓여있다. 비가 오면 블록 사이에 빗물이 고인다.

비는 충분히 많이 온다. 고이는 빗물의 총량은 얼마일까?

입력 :
첫 번째 줄에는 2차원 세계의 세로 길이 H과 2차원 세계의 가로 길이 W가 주어진다. (1 ≤ H, W ≤ 500)
두 번째 줄에는 블록이 쌓인 높이를 의미하는 0이상 H이하의 정수가 2차원 세계의 맨 왼쪽 위치부터 차례대로 W개 주어진다.
따라서 블록 내부의 빈 공간이 생길 수 없다. 또 2차원 세계의 바닥은 항상 막혀있다고 가정하여도 좋다.

결과 :
2차원 세계에서는 한 칸의 용량은 1이다. 고이는 빗물의 총량을 출력하여라.
빗물이 전혀 고이지 않을 경우 0을 출력하여라.
'''
import sys
input = sys.stdin.readline

row, col = map(int, input().split())
block_list = list(map(int, input().split()))

world = [[0 for _ in range(col)] for _ in range(row)]

for i in range(col):
    for j in range(block_list[i]):
        world[row-1-j][i] = 1

rain_sum = 0

cur = 0
while(cur < col-1):
    end_point = col
    # 현재 벽 보다 더 큰 벽이 있으면 그곳에서 멈춘다.
    cur_height = block_list[cur]
    while(cur_height > 0):
        if(end_point != col):
            break
        for i in range(cur+1, col):
            if block_list[i] >= cur_height :
                end_point = i
                break
        cur_height = cur_height - 1

    if end_point == col:
        end_point = col -1
    min_height = min(block_list[cur], block_list[end_point])

    for i in range(cur+1, end_point):
        for j in range(min_height):
            if (world[row-1-j][i] != 1):
                rain_sum = rain_sum + 1
    cur = end_point

print(rain_sum)