'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/10/11
boj.kr/2075
N 번째 큰 수
'''
import sys
import heapq
input = sys.stdin.readline

N = int(input())

num_list = []

for i in range(N):
    if i == 0:
        for item in list(map(int, input().split())):
            heapq.heappush(num_list, item)
    else :
        for item in list(map(int, input().split())):
            if item > num_list[0]:
                heapq.heappop(num_list)
                heapq.heappush(num_list, item)

num_list.sort()

print(num_list[0])