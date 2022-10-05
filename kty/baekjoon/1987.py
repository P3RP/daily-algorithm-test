'''
******* 문제 푼 후 느낀 것 *********
pypy3 으로 하면 통과하고, python3 으로 하면 시간초과가 발생한다.

그리고 처음에는 dict이 list를 사용하는것 보다 더 빠를 것 같아서 dict을 사용했는데
내부적으로 해시테이블을 사용해서 저장하여 시간이 list에서 직접접근하는것보다 시간이 오래걸린다고 한다. 

그래서 알파벳 사용 여부를 dict를 이용한 것이 아닌 list로 알파벳을 26개를 저장해서 1,0로 구분했다.
이전에도 비슷한 것을 해보았는데, 다음에는 꼭 기억하고 풀 수 있도록 하자!!
'''

'''
2022/09/04
boj.kr/1987
알파벳
'''
import sys
input = sys.stdin.readline

move = [(0,1), (1,0), (-1,0), (0, -1)]

R, C = map(int, input().split())

alpha_map = []

for _ in range(R):
    alpha_map.append(input().strip())


visited = [0 for _ in range(27)]

max_move = 0
def dfs(start, count = 1):
    global alpha_map
    global max_move
    global visited
    (x, y) = start 


    for nx,ny in move:
        new_x = x + nx
        new_y = y + ny
        if 0 <= new_x < R and 0 <= new_y < C:
            if visited[ord(alpha_map[new_x][new_y]) - ord('A')] != 1:
                visited[ord(alpha_map[new_x][new_y]) - ord('A')] = 1
                dfs((new_x, new_y), count = count + 1)
                visited[ord(alpha_map[new_x][new_y]) - ord('A')] = 0
            else :
                max_move = max(max_move, count)

visited[ord(alpha_map[0][0]) - ord('A')] = 1
dfs((0,0))
print(max_move)
            

