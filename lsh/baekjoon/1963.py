import sys
from collections import deque
input = sys.stdin.readline

INF = 1e9
end = 10000
chk = [True] * end
chk[0] = False
chk[1] = True

i = 2
while i < end:
    for j in range(i * 2, end, i):
        chk[j] = False
    i += 1


def chg_num(target, loc, num):
    next = list(str(target))
    next[loc] = str(num)
    return int(''.join(next))
    


def bfs(start, target):
    if start == target:
        return 0

    que = deque([(start, 0)])
    cache = set([start])

    while que:
        now, cnt = que.popleft()
        cache.add(now)

        for i in range(1, 10):
            next = chg_num(now, 0, i)
            if next in cache:
                continue
            if next == target:
                return cnt + 1
            if not chk[next]:
                continue
            que.append((next, cnt + 1))

        for i in range(10):
            for loc in range(1, 4):
                next = chg_num(now, loc, i)
                if next in cache:
                    continue
                if next == target:
                    return cnt + 1
                if not chk[next]:
                    continue
                que.append((next, cnt + 1))

T = int(input())
for _ in range(T):
    now, target = map(int, input().split())
    print(bfs(now, target))
