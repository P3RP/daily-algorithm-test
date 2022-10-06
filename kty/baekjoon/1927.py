'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/10/06
boj.kr/1927
최소 힙
'''
import heapq
import sys

input = sys.stdin.readline

N = int(input())

min_q = []
for _ in range(N):
    value = int(input())
    if value == 0:
        if len(min_q) > 0 :
            print(heapq.heappop(min_q))
        else :
            print(0)
    else :
        heapq.heappush(min_q, value)