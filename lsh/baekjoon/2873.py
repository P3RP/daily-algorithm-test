import sys
input = sys.stdin.readline

row, col = map(int, input().split())
c_row = row % 2
c_col = col % 2

board = [list(map(int, input().split())) for _ in range(row)]

move_r = ['D', 'U']
move_c = ['R', 'L']

# 행 : 홀 / 열 : 홀 || 행 : 홀 / 열 : 짝
if c_row:
    answer = (move_c[0] * (col - 1) + 'D' + move_c[1] * (col - 1) + 'D') * (row // 2)
    answer += move_c[0] * (col - 1)

# 행 : 짝 / 열 : 홀
elif c_col:
    answer = (move_r[0] * (row - 1) + 'R' + move_r[1] * (row - 1) + 'R') * (col // 2)
    answer += move_r[0] * (row - 1)

# 행 : 짝 / 열 : 짝
else:
    # 초기 설정
    answer = ''
    path = [((1, 0), 'D'), ((0, 1), 'R'), ((-1, 0), 'U'), ((0, 1), 'R')]
    now = 0

    # 최솟값 위치 찾는 과정
    m_pos = [-1, -1]
    m_value = 1001
    for i in range(row):
        if i % 2:
            start = 0
        else:
            start = 1
        for j in range(start, col, 2):
            value = board[i][j]
            if value < m_value:
                m_value = value
                m_pos = [i, j]

    # 1자로 왔다 갔다 처리
    answer += (move_c[0] * (col - 1) + 'D' + move_c[1] * (col - 1) + 'D') * (m_pos[0] // 2)

    # 지그재그 처리
    x, y = 2 * (m_pos[0] // 2), 0
    while x != (m_pos[0] // 2 * 2) + 1 or y != col - 1:
        if x + path[now][0][0] == m_pos[0] and y + path[now][0][1] == m_pos[1]:
            y += 1
            answer += 'R'
        else:
            x += path[now][0][0]
            y += path[now][0][1]
            answer += path[now][1]
            now += 1
            now %= 4

    # 1자로 왔다 갔다 처리
    answer += ('D' + move_c[1] * (col - 1) + 'D' + move_c[0] * (col - 1)) * ((row // 2) - (m_pos[0] // 2) - 1)

print(answer)



# # 이동 방향
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# name = ['R', 'D', 'L', 'U']

# def search(board, x, y, answer):
#     # 이동 불가 경우
#     if x < 0 or x >= row: return
#     if y < 0 or y >= col: return
#     if not board[x][y]: return
#     if not sum([sum(x) for x in board]):
#         if x != row - 1 or y != col - 1:
#             return
#     if len(result) > 0: return
    
#     board[x][y] = 0

#     # 성공한 경우
#     if x == (row - 1) and y == (col - 1):
#         if not sum([sum(x) for x in board]):
#             result.append(answer)
#         return

#     for i in range(4):
#         if x + dx[i] < 0 or x + dx[i] >= row: continue
#         if y + dy[i] < 0 or y + dy[i] >= col: continue
#         if not board[x + dx[i]][y + dy[i]]: continue

#         search([x[:] for x in board], x + dx[i], y + dy[i], answer + name[i])
#         if len(result) > 0: continue

#         # search(board, x + dx[i], y + dy[i], answer + name[i])


# if not c_row and not c_col:
#     m_row = -1
#     m_col = -1
#     m_value = INF

#     for i in range(row):
#         for j in range(0, col, 2):
#             value = board[i][((i + 1) % 2) + j]
#             if value < m_value:
#                 m_value = value
#                 m_row = i
#                 m_col = ((i + 1) % 2) + j
#     board[m_row][m_col] = 0

# search(board, 0, 0, '')
# print(result[0])

# exit()
