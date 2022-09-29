'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/09/29
boj.kr/17615
볼 모으기
'''
import sys
input = sys.stdin.readline

def solution(move, balls):
    start = len(balls)-1
    end = len(balls)-1

    
    count = 0
    while(1):
        # 두 공을 옮긴다.

        # 옮길 공의 시작점을 찾는다.
        while(start > 0):
            if balls[start] != move and balls[start-1] == move:
                start -= 1
                break
            start -= 1
        # 바뀔 공의 위치를 찾는다.
        while(end > 0):
            if balls[end] != move and balls[end-1] == move:
                break
            end -= 1

        if start == 0 and end == 0:
            break

        balls[start] = balls[end]
        balls[end] = move
        count += 1
    return count


N = int(input())
balls = list(input().strip())

red_count = 0
blue_count = 0

for ball in balls:
    if ball == 'R':
        red_count += 1
    else :
        blue_count += 1

count = min(red_count, blue_count)

# 왼쪽부터 세기
left_count = 0
right_count = 0
for i in range(N):
    if balls[i] != balls[0] :
        break
    left_count += 1

count = min(red_count-left_count, count) if balls[0] == 'R' else  min (blue_count - left_count, count)

for i in range(N-1, -1, -1):
    if balls[N-1] != balls[i]:
        break
    right_count += 1


count = min(red_count-right_count, count) if balls[N-1] == 'R' else  min (blue_count - right_count, count)

print(count)