'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/10/11
boj.kr/2668
숫자고르기
'''
import sys

input = sys.stdin.readline

N = int(input())
num_list = [0]
for _ in range(N):
    num_list.append(int(input()))

def dfs(find, start, visited, num_list):
    if find == start:
        return True
    if visited[start] == 1:
        return False
    visited[start] = 1
    return dfs(find, num_list[start], visited=visited, num_list=num_list)

result = []
for i in range(1, N+1):
    if dfs(i, num_list[i], visited=[0 for _ in range(N+1)], num_list=num_list):
        result.append(i)

print(len(result))
for n in result:
    print(n)

