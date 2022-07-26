'''
******* 문제 푼 후 느낀 것 *********
bfs라 생각하는것이 좀 오래 걸렸다.
흠.. 
어떤 것에 대해서 반복적으로 확인하는데, 최소 몇번이 걸리는지 확인할떄는 
bfs 를 사용하는 것이 좋다. -> 물론 패턴으로 찾을 수 있다면 그것이 베스트
dfs는 가중치가 있고, 그것에 대해 최솟값이나 최댓값을 찾을떄 활용하는 것 같다.
'''

'''
2022/05/25
boj.kr/1697
숨바꼭질

문제 :
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력 :
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

결과 :
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
'''
import sys
import copy
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
# bfs

checked = [0 for _ in range(100001)]
queue = deque()

queue.append(n)
checked.append(n)
count = 0


checked[n] = 1
while(1):
    if checked[k]:
        break
    else:
        # temp_queue, queue 2개를 두고, 하나는 빼기만하고, 하나는 넣기만 한 뒤
        # 마지막에 다시 queue 에 넣어주는 것으로 구현했는데 이때 deppcopy를 사용하였는데
        # 이것이 bigO 가 O(n)
        # 그래서 시간초과가 자꾸 발생하였다.
        size = len(queue)
        count += 1
        for _ in range(size):
            item = queue.popleft()
            if item < 100000 and not checked[item+1]:
                queue.append(item+1)
                checked[item+1] = 1
            if item*2 <= 100000 and not checked[item*2]:
                queue.append(item*2)
                checked[item*2] = 1
            if item > 0 and not checked[item-1]:
                queue.append(item-1)
                checked[item-1] = 1

print(count)

# 재귀로 풀게 되면 recursion error가 발생한다
'''
min_count = 200000

def dfs(now, count):
    global min_count
    if count > min_count:
        return
    if k*2 < now or now < 0:
        return
    elif k == now:
        min_count = min(min_count, count)
    else:
        dfs(now*2, count+1)
        dfs(now-1, count+1)
        dfs(now+1, count+1)
dfs(n, 0)
'''
