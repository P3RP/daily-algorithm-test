'''
******* 문제 푼 후 느낀 것 *********
하... 완탐 너무 어렵다
이거 완탐인지 확인하는 것은 문제에서 주어진 범위를 보고, 전부다 탐색했을때 가능할 것 같으면 해야될 것 같다.
그리고 완탐에서는 패턴을 찾고, 그 패턴을 전부 확인하는 것이 중요한 것 같다. 

'''

'''
2022/05/16
boj.kr/1451
직사각형으로 나누기

문제 :
세준이는 N*M크기로 직사각형에 수를 N*M개 써놓았다.
세준이는 이 직사각형을 겹치지 않는 3개의 작은 직사각형으로 나누려고 한다. 각각의 칸은 단 하나의 작은 직사각형에 포함되어야 하고, 각각의 작은 직사각형은 적어도 하나의 숫자를 포함해야 한다.
어떤 작은 직사각형의 합은 그 속에 있는 수의 합이다. 입력으로 주어진 직사각형을 3개의 작은 직사각형으로 나누었을 때, 각각의 작은 직사각형의 합의 곱을 최대로 하는 프로그램을 작성하시오.

입력 :
첫째 줄에 직사각형의 세로 크기 N과 가로 크기 M이 주어진다. 둘째 줄부터 직사각형에 들어가는 수가 가장 윗 줄부터 한 줄에 하나씩 M개의 수가 주어진다. 
N과 M은 50보다 작거나 같은 자연수이고, 직사각형엔 적어도 3개의 수가 있다. 또, 직사각형에 들어가는 수는 한 자리의 숫자이다.
결과 :
세 개의 작은 직사각형의 합의 곱의 최댓값을 출력한다.
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

whole_rec = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(N):
    line = input()
    for j in range(M):
        whole_rec[i+1][j+1] = int(line[j])


max_value = -1


def sum(startX, endX, startY, endY):
    value = 0
    for j in range(startX, endX+1):
        for i in range(startY, endY+1):
            value += whole_rec[i][j]
    return value


# 6가지 경우
# 1 경우
for i in range(1, N):
    for j in range(1, M):
        rec1 = sum(1, j, 1, i)
        rec2 = sum(j+1, M, 1, i)
        rec3 = sum(1, M, i+1, N)
        max_value = max(max_value, rec1*rec2*rec3)
# 2 경우
for i in range(1, N):
    for j in range(1, M):
        rec1 = sum(1, M, 1, i)
        rec2 = sum(1, j, i+1, N)
        rec3 = sum(j+1, M, i+1, N)
        max_value = max(max_value, rec1*rec2*rec3)

# 3경우
for i in range(1, N):
    for j in range(1, M):
        rec1 = sum(1, j, 1, i)
        rec2 = sum(1, j, i+1, N)
        rec3 = sum(j+1, M, 1, N)
        max_value = max(max_value, rec1*rec2*rec3)

# 4
for i in range(1, N):
    for j in range(1, M):
        rec1 = sum(1, j, 1, N)
        rec2 = sum(j+1, M, 1, i)
        rec3 = sum(j+1, M, i+1, N)
        max_value = max(max_value, rec1*rec2*rec3)

# 5
for i in range(1, N):
    for j in range(i+1, N):
        rec1 = sum(1, M, 1, i)
        rec2 = sum(1, M, i+1, j)
        rec3 = sum(1, M, j+1, N)
        max_value = max(max_value, rec1*rec2*rec3)

# 6
for i in range(1, M):
    for j in range(i+1, M):
        rec1 = sum(1, i, 1, N)
        rec2 = sum(i+1, j, 1, N)
        rec3 = sum(j+1, M, 1, N)
        max_value = max(max_value, rec1*rec2*rec3)

print(max_value)
