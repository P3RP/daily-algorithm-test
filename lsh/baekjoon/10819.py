import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
nums = list(sorted(map(int, input().split())))

# ==================================================
# 전체 경우 탐색 버전
# ==================================================
answer = -1
for case in permutations(nums, N):
    chk = 0
    for i in range(len(case) - 1):
        chk += abs(case[i] - case[i + 1])
    answer = max(answer, chk)
print(answer)
exit()


# ==================================================
# 경우 나눠서 풀기 버전
# 큰 그룹, 작은 그룹 나누기
# 전체 개수가 홀수개, 짝수개인 경우 서로 나눠서 풀기
# 홀수 개인 경우, 큰 그룹이 더 많은지, 작은 그룹이 더 많은지 골라야 함
# ==================================================
down = nums[:N // 2]
up = nums[N // 2:]
answer = (sum(up) * 2) - (sum(down) * 2)
if N % 2:
    if up[0] - up[1] > down[-1] - up[0]:
        answer -= up[0]
        answer -= up[1]
    else:
        answer -= up[0] * 3
        answer += down[-1]
else:
    answer -= up[0]
    answer += down[-1]
    
print(answer)
