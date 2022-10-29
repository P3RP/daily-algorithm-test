'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/10/07
boj.kr/2164
카드2
'''
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

q = deque()

if N == 1:
    print(N)

else :
    for i in range(N):
        q.append(i+1)

    for _ in range(N):
        trash = q.popleft()

        if len(q) == 1:
            print(q[0])
            break

        back = q.popleft()
        q.append(back)