'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/10/17
boj.kr/2304
N 번째 큰 수
'''
import sys
input = sys.stdin.readline

N = int(input())

bar_list = []
for _ in range(N):
    pos, height = map(int, input().split())
    bar_list.append((pos, height))

bar_list.sort()

# 왼쪽 넓이 구하기
answer = 0
before_pos, before_height = bar_list[0]
before_pos -= 1
before_height = 0
for i in range(0, N):
    now_pos, now_height = bar_list[i]

    if now_height >= before_height:
        answer += before_height*abs(now_pos - before_pos-1)
        answer += now_height
        before_pos = now_pos
        before_height = now_height
    

before_pos, before_height = bar_list[-1]
for i in range(N-2, -1, -1):
    now_pos, now_height = bar_list[i]

    if now_height > before_height:
        answer += before_height*abs(now_pos - before_pos)
        before_pos = now_pos
        before_height = now_height

print(answer)
 

