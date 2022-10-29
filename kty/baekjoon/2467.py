'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/10/010
boj.kr/2467
용액
'''
import sys
input = sys.stdin.readline

N = int(input())

solution_list = list(map(int, input().split()))

start = 0
end = N-1

pos = (0, 0)
min_abs = sys.maxsize

while(start < end):
    new_v = solution_list[start] + solution_list[end]
    if min_abs > abs(new_v):
        min_abs = abs(new_v)
        pos = (start, end)
    if new_v == 0:
        break
    elif new_v > 0 :
        end -= 1
    else :
        start += 1

start, end = pos
print(solution_list[start], solution_list[end])