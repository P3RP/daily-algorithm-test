'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/10/25
boj.kr/15989
1,2,3 더하기 4
'''
import sys
input = sys.stdin.readline


answer = [0 for _ in range(10001)]

answer[1] = 1
answer[2] = 2
answer[3] = 3
answer[4] = 4

for i in range(5, 10001):
    if i % 3 == 0 or i % 2 == 0:
        answer[i] = answer[i-1] + 2
    else :
        answer[i] = answer[i-1] + 1

N = int(input())

for _ in range(N):
    print(answer[int(input())])

