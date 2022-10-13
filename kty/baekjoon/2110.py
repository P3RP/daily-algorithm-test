'''
******* 문제 푼 후 느낀 것 *********
꼭 다시 풀어보기...
너무 어려웠다 ㅠㅜ
'''

'''
2022/10/13
boj.kr/2110
공유기 설치
'''
import sys
input = sys.stdin.readline

N, C = map(int, input().split())

house_list = []

for _ in range(N):
    house_list.append(int(input()))

house_list.sort()

min_dist = 0
max_dist = house_list[N-1]
answer = 0
while(min_dist <= max_dist):
    mid_dist = (min_dist + max_dist) // 2

    last_installed = 0
    cnt = 1
    for i in range(1, N):
        if house_list[i] - house_list[last_installed] >= mid_dist:
            cnt += 1
            last_installed = i
    
    if cnt >= C:
        answer = mid_dist
        min_dist = mid_dist + 1
    elif cnt < C :
        max_dist = mid_dist - 1

print(answer)