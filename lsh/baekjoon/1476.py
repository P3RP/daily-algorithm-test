import sys
input = sys.stdin.readline

E, S, M = map(int, input().split())


answer = 0
while E > 0 or S > 0 or M > 0:
    if not E:
        E += 15
    if not S:
        S += 28
    if not M:
        M += 19

    E -= 1
    S -= 1
    M -= 1
    answer += 1

print(answer)
