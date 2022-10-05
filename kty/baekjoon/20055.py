'''
******* 문제 푼 후 느낀 것 *********
문제를 잘못읽고 슬라이딩 윈도우 움직이는 방향을 잘못 선정해서 오래걸리게 되었다.

pypy3로 했을때는 로봇들을 배열로 하여 일일이 반복문을 이용해서 옮겨줬다. 
하지만 이것이 시간초과의 원인이 되었고, 이를 deque를 이용하여 pop과 appendleft 를 이용하도록 변경하여 python3 으로 통과할 수 있었다.
'''

'''
2022/09/05
boj.kr/20055
컨베이어 벨트 위의 로봇
'''
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

belt = list(map(int, input().split()))

robot = deque([0 for _ in range(N)])
# 벨트를 먼저 회전시키고
# 로봇이 한칸씩 이동한다(이동할 수 없다면 가만히 있는다)
# 로봇을 올리는 위치에 올린다(내구도가 0이 아니라면)
# 내구도가 0인 칸의 개수가 k개 이상이면 종료한다

# 슬라이딩 윈도우? -> 이게 무조건 더 빠를 듯?
# 아니면 덱?

start = 0
durability = 0
count = 0

while(durability < K):
    
    count += 1
    # 벨트 회전
    start = (start - 1) % (2*N)
    
    # 벨트가 이동했을때 로봇이 내리는 위치에 가면 바로 내린다
    robot.pop()
    robot.appendleft(0)
    robot[N-1] = 0

    # 로봇 한칸씩 이동
    for i in range(N-2, -1, -1):
        # 로봇이 있는 경우
        if robot[i] == 1:
            next_belt_pos = (start+i+1) % (2*N)
            # 옆 칸에 로봇이 없고, 내구성이 0 이상일때 이동시킨다
            if robot[i+1] == 0 and belt[next_belt_pos] > 0 :
                robot[i] = 0
                robot[i+1] = 1

                # 내구성 뺴기
                belt[next_belt_pos] -= 1
                if belt[next_belt_pos] == 0 :
                    durability += 1
                # 만약 내리는 위치에 이동했다면 바로 내린다
    robot[N-1] = 0 

    # 로봇 올리기
    if belt[start] > 0 :
        belt[start] -= 1
        if belt[start] == 0:
            durability += 1
        robot[0] = 1

print(count)