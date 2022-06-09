import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

END = 100000
cache = [0] * (END + 1)
def bfs():
    queue = deque([N])

    while queue:
        x = queue.popleft()

        if x == K:
            return cache[x]
        
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= END and not cache[nx]:
                cache[nx] = cache[x] + 1
                queue.append(nx)


print(bfs())






# def chk(now, cnt):
#     if now == N:
#         return cnt
    
#     if abs(now - N) == 1:
#         return cnt + 1

#     if now < N:
#         return cnt + N - now
    
#     if now <= 1:
#         return 1e9

#     if now % 2:
#         cnt = min(chk(now // 2, cnt + 2), chk(now // 2 + 1, cnt + 2))
#     else:
#         cnt = chk(now // 2, cnt + 1)
#     return cnt

# if K < N:
#     answer = N - K
# else:
#     answer = chk(K, 0)
# print(answer)



# answer = 1e9
# def dfs(now, cnt):
#     print(now, cnt)
#     global chk
#     global answer

#     # 도착한 경우
#     if now == K:
#         answer = min(answer, cnt)
#     elif now < 0 or now > 100000:
#         return
#     else:
#         dfs(now - 1, cnt + 1)

#         if now < K:
#             dfs(now + 1, cnt + 1)

#         if now != 0 and now < K:
#             dfs(now * 2, cnt + 1)

# answer = 0
# while N * 2 < K:
#     answer += 1
#     N *= 2
# a = abs(N * 2 - 2 - K)
# b = abs(N * 2 - K)
# c = abs(N * 2 + 2 - K)
# m = min(a, b, c)
# if m == a:
#     answer += 2
#     answer += a
# elif m == b:
#     answer += 1
#     answer += b
# else:
#     answer += 2
#     answer += c


# print(a, b, c)
# print(N)
# print(answer)