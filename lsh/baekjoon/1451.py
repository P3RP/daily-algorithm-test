import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
answer = -1

# 세로로 나누기
all, sep = N, M
for i in range(1, sep - 1):
    for j in range(i, sep):
        num1 = 0
        for row in range(all):
            num1 += sum(board[row][:i])

        num2 = 0
        for row in range(all):
            num2 += sum(board[row][i:j])
        
        num3 = 0
        for row in range(all):
            num3 += sum(board[row][j:])

        result = num1 * num2 * num3
        if result > answer:
            answer = result

# 가로로 나누기
all, sep = M, N
for i in range(1, sep - 1):
    for j in range(i, sep):
        num1 = 0
        for row in range(i):
            num1 += sum(board[row])

        num2 = 0
        for row in range(i, j):
            num2 += sum(board[row])
        
        num3 = 0
        for row in range(j, N):
            num3 += sum(board[row])

        result = num1 * num2 * num3
        if result > answer:
            answer = result

# T로 자르기: Case 1 / T 정방향
for i in range(1, N):
    for j in range(1, M):
        num1 = 0
        for row in range(i):
            num1 += sum(board[row])

        num2 = 0
        num3 = 0
        for row in range(i, N):
            num2 += sum(board[row][:j])
            num3 += sum(board[row][j:])

        result = num1 * num2 * num3
        if result > answer:
            answer = result

# T로 자르기: Case 2 / T 상하반전
for i in range(1, N):
    for j in range(1, M):
        num1 = 0
        for row in range(i, N):
            num1 += sum(board[row])

        num2 = 0
        num3 = 0
        for row in range(i):
            num2 += sum(board[row][:j])
            num3 += sum(board[row][j:])

        result = num1 * num2 * num3
        if result > answer:
            answer = result

# T로 자르기: Case 3 / T 90도 시계방향
for i in range(1, N):
    for j in range(1, M):
        num1 = 0
        for row in range(N):
            num1 += sum(board[row][j:])

        num2 = 0
        for row in range(i):
            num2 += sum(board[row][:j])

        num3 = 0
        for row in range(i, N):
            num3 += sum(board[row][:j])

        result = num1 * num2 * num3
        if result > answer:
            answer = result

# T로 자르기: Case 3 / T 90도 반시계방향
for i in range(1, N):
    for j in range(1, M):
        num1 = 0
        for row in range(N):
            num1 += sum(board[row][:j])

        num2 = 0
        for row in range(i):
            num2 += sum(board[row][j:])

        num3 = 0
        for row in range(i, N):
            num3 += sum(board[row][j:])

        result = num1 * num2 * num3
        if result > answer:
            answer = result

print(answer)
exit()


# =============================================================================
# 계속해서 고민한 흔적
# - 부분 합 개념 사용
# - 모든 케이스에 대해서 고민을 실패함
# =============================================================================
s_num = [[-1] * M for _ in range(N)]
s_num[0][0] = board[0][0]

for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            continue
        calc = board[i][j]
        if i > 0:
            calc += s_num[i - 1][j]
        if j > 0:
            calc += s_num[i][j - 1]
        if i > 0 and j > 0:
            calc -= s_num[i - 1][j - 1]
        s_num[i][j] = calc


print(s_num)

answer = -1


# 맨 오른쪽 줄 제외한 것이 한 조각
for i in range(N - 1):
    calc = s_num[N - 1][M - 2]
    calc *= s_num[i][M - 1] - s_num[i][M - 2]
    calc *= s_num[N - 1][M - 1] - s_num[i][M - 1] - s_num[N - 1][M - 2] + s_num[i][M - 2]
    if calc > answer:
        answer = calc


# 맨 밑 줄 제외한 것이 한 조각
for j in range(M - 1):
    calc = s_num[N - 2][M - 1]
    calc *= s_num[N - 1][i] - s_num[N - 2][i]
    calc *= s_num[N - 1][M - 1] - s_num[N - 2][M - 1] - s_num[N - 1][i] + s_num[N - 2][i]
    if calc > answer:
        answer = calc
    print('i', i, calc)


for i in range(N - 1):
    for j in range(M - 1):
        print(i, j, board[i][j])
        # 1번 Case
        calc = s_num[i][j]
        calc *= s_num[i][M - 1] - s_num[i][j]
        calc *= s_num[N - 1][M - 1] - s_num[i][M - 1]
        print(calc)
        if calc > answer:
            answer = calc

        # 2번 Case
        calc = s_num[i][j]
        calc *= s_num[N - 1][j] - s_num[i][j]
        calc *= s_num[N - 1][M - 1] - s_num[N - 1][j]
        print(calc)
        if calc > answer:
            answer = calc



print(s_num)
print(answer)
