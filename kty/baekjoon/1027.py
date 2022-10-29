'''
******* 문제 푼 후 느낀 것 *********
문제를 차분하게 생각할 수 있도록 하자!
또한 문제를 꼼꼼히 읽고 꼭 생각하고 풀자!
'''

'''
2022/10/15
boj.kr/1027
고층 건물
'''
import sys
input = sys.stdin.readline

N = int(input())

building_list = [0]

building_list += list(map(int, input().split()))

lean = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(i+1, N+1):
        lean[i][j] = (building_list[i] - building_list[j]) / (i-j)
        lean[j][i] = (building_list[j] - building_list[i]) / (j-i)

max_count = 0
for i in range(1,N+1):
    count = 0
    # 왼쪽은 반대로 가면서 기울기가 감소해야 한다.
    if i > 1:
        before = lean[i][i-1]
        count += 1
        for j in range(i-2, 0, -1):
            now = lean[i][j]
            if before <= now:
                continue
            before = now
            count += 1
        
    # 오른쪽은 기울기가 점점 증가해야한다.
    if i < N:
        before = lean[i][i+1]
        count += 1
        for j in range(i+2, N+1):
            now = lean[i][j]
            if before >= now:
                continue
            before = now
            count += 1
    max_count = max(max_count, count)

print(max_count)