'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/08/24
boj.kr/1238
파티

문제 :
N개의 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있다.

어느 날 이 N명의 학생이 X (1 ≤ X ≤ N)번 마을에 모여서 파티를 벌이기로 했다. 
이 마을 사이에는 총 M개의 단방향 도로들이 있고 i번째 길을 지나는데 Ti(1 ≤ Ti ≤ 100)의 시간을 소비한다.

각각의 학생들은 파티에 참석하기 위해 걸어가서 다시 그들의 마을로 돌아와야 한다. 
하지만 이 학생들은 워낙 게을러서 최단 시간에 오고 가기를 원한다.

이 도로들은 단방향이기 때문에 아마 그들이 오고 가는 길이 다를지도 모른다. 
N명의 학생들 중 오고 가는데 가장 많은 시간을 소비하는 학생은 누구일지 구하여라.

입력 :
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 10,000), X가 공백으로 구분되어 입력된다. 
두 번째 줄부터 M+1번째 줄까지 i번째 도로의 시작점, 끝점, 그리고 이 도로를 지나는데 필요한 소요시간 Ti가 들어온다. 
시작점과 끝점이 같은 도로는 없으며, 시작점과 한 도시 A에서 다른 도시 B로 가는 도로의 개수는 최대 1개이다.

모든 학생들은 집에서 X에 갈수 있고, X에서 집으로 돌아올 수 있는 데이터만 입력으로 주어진다.

결과 :
첫 번째 줄에 N명의 학생들 중 오고 가는데 가장 오래 걸리는 학생의 소요시간을 출력한다.
'''
import sys
import heapq

input = sys.stdin.readline

# N 명, M 길, X 마을
N, M, X = map(int, input().split())

load = [[] for _ in range(N+1)]

# 특정 점에서 각 점까지 가는 거리는 그냥 구해도 된다.
# 모든 점에서 특정 점까지 가는 거리의 최소값?

for _ in range(M):
    start, end, time = map(int, input().split())
    load[start].append((time, end))

# 큐에서 거리가 가장 짧은 것들을 꺼낸다.
# 더 짧다면 해당 값을 업데이트하고, 큐에 넣어준다.
# 1 2 3 4 -> 2 로 가는 
# 그리고 다시 2 에서 나머지로 가는 거리
# 이때 문ㅁ제는 1,2,3,4 -> 2 로 가는 최단거리를 어떻게 찾을것인지?

def dijkstra(start) :
    global N
    global load
    pq = []
    dist = [sys.maxsize for _ in range(N+1)]
    heapq.heappush(pq, (0, start))
    dist[start] = 0

    while(pq):
        cur_dist, cur_v = heapq.heappop(pq)
        # 현재 들어온 거리가 더 크다면 확인해볼 필요가 없음
        if cur_dist > dist[cur_v]:
            continue
        for next_dist, next_v in load[cur_v]:
            new_dist = cur_dist + next_dist
            if new_dist < dist[next_v]:
                dist[next_v] = new_dist
                heapq.heappush(pq, (new_dist, next_v))
    return dist

result = 0
for i in range(1, N+1):
    go = dijkstra(i)
    back = dijkstra(X)
    result = max(result, go[X] + back[i])

print(result)