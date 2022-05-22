import sys
input = sys.stdin.readline

n = int(input())
cache = [-1, 1, 2, 4]
target = [int(input()) for _ in range(n)]

for i in range(4, max(target) + 1):
    cache.append(cache[i - 1] + cache[i - 2] + cache[i - 3])

for i in target:
    print(cache[i])
