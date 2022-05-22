import sys
input = sys.stdin.readline

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
visited[0] = True

answer = 1e9
def dfs(visited, now, cost):
    global answer

    if all(visited):
        if costs[now][0]:
            answer = min(answer, cost + costs[now][0])
    
    for i in range(N):
        if i == now:
            continue

        if visited[i]:
            continue
        
        if not costs[now][i]:
            continue

        n_visited = visited[:]
        n_visited[i] = True
        dfs(n_visited, i, cost + costs[now][i])

dfs(visited=visited, now=0, cost=0)
print(answer)
