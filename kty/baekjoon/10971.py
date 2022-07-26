'''
******* 문제 푼 후 느낀 것 *********
그냥 다른 그래프 문제는 끝까지 가서 가능한지 확인하는 것이기 때문에
방문한 곳을 공통적으로 체크하면서 나가면 된다. 

하지만 백트래킹 같은 경우에는 다시 돌아오고, 지났던 곳을 빼고 다시 가야하기 떄문에 이전에 넣었던 것을 빼는 작업이 필요하다.

이때 이전에 풀어보았던 늑대 문제가 있는데, 늑대 문제는 늑대들을 계속 데리고 다닌다. 트리의 반대로 올라가도 늑대가 사라지지 않는다.
그래서 deepcopy 를 이용하여 visited를 관리하고, 늑대를 다시 빼주는 작업을 하지 않았다. 

하지만 여기서는 뒤로 돌아가면 방문했던 내역이 사라지기 때문에 deepcopy를 쓰지 않아도 되고, 뒤로 돌아오면 다시이를 빼주는 작업을 수행해야한다.
'''

'''
2022/05/23
boj.kr/10971
외판원 순회 2

문제 :
외판원 순회 문제는 영어로 Traveling Salesman problem (TSP) 라고 불리는 문제로 computer science 분야에서 가장 중요하게 취급되는 문제 중 하나이다.
여러 가지 변종 문제가 있으나, 여기서는 가장 일반적인 형태의 문제를 살펴보자.

1번부터 N번까지 번호가 매겨져 있는 도시들이 있고, 도시들 사이에는 길이 있다. (길이 없을 수도 있다)
이제 한 외판원이 어느 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회 여행 경로를 계획하려고 한다. 단, 한 번 갔던 도시로는 다시 갈 수 없다.
(맨 마지막에 여행을 출발했던 도시로 돌아오는 것은 예외) 이런 여행 경로는 여러 가지가 있을 수 있는데, 가장 적은 비용을 들이는 여행 계획을 세우고자 한다.

각 도시간에 이동하는데 드는 비용은 행렬 W[i][j]형태로 주어진다. W[i][j]는 도시 i에서 도시 j로 가기 위한 비용을 나타낸다.
비용은 대칭적이지 않다. 즉, W[i][j] 는 W[j][i]와 다를 수 있다. 모든 도시간의 비용은 양의 정수이다. W[i][i]는 항상 0이다.
경우에 따라서 도시 i에서 도시 j로 갈 수 없는 경우도 있으며 이럴 경우 W[i][j]=0이라고 하자.

N과 비용 행렬이 주어졌을 때, 가장 적은 비용을 들이는 외판원의 순회 여행 경로를 구하는 프로그램을 작성하시오.

입력 :
첫째 줄에 도시의 수 N이 주어진다. (2 ≤ N ≤ 10) 다음 N개의 줄에는 비용 행렬이 주어진다. 각 행렬의 성분은 1,000,000 이하의 양의 정수이며,
갈 수 없는 경우는 0이 주어진다. W[i][j]는 도시 i에서 j로 가기 위한 비용을 나타낸다.

항상 순회할 수 있는 경우만 입력으로 주어진다.

결과 :
첫째 줄에 외판원의 순회에 필요한 최소 비용을 출력한다.
'''

import sys
import copy
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, input().split()))

min_value = 9999999999


def dfs(start, fix_start, count, visited, value):
    global min_value
    print(visited)
    if count == n:
        if start == fix_start:
            min_value = min(min_value, value)
        return
    elif value > min_value:
        return
    else:
        for i in range(len(graph[start])):
            # 가중치가 0이 아니고, 방문하지 않은 경우에만
            if graph[start][i] != 0 and visited[i] == False:
                visited[i] = True
                dfs(i, fix_start, count+1,
                    visited, value+graph[start][i])
                visited[i] = False


for i in range(n):
    visited = [False for _ in range(n)]
    dfs(i, i, 0, visited, 0)

print(min_value)
