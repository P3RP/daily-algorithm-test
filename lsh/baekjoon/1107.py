import sys
input = sys.stdin.readline

N = int(input().rstrip())
n_trouble = int(input())
trouble = set(input().rstrip().split())
now = 100

cnt = abs(N - now)
for i in range(1000001):
    if set(str(i)) & trouble:
        continue

    n_cnt = abs(i - N)      # +/-로 이동
    n_cnt += len(str(i))    # 번호 눌러서 채널
    if n_cnt < cnt:
        cnt = n_cnt

    # # 속도를 위해 종료 조건 추가
    # # 이동 횟수가 늘어나는 경우 종료
    # 생각해보니까 예외 조건 존재함
    # if n_cnt > cnt:
    #     break

# 이동버튼으로만 이동한 경우와 비교해서 출력
print(cnt)
exit()



# 번호를 찍은 후 이동하는 경우
move = {
    'n': '',
    'up': None,
    'down': None,
}
move_cnt = 0
for idx, n in enumerate(N):
    # 이동 버튼으로 이동한 것보다 이미 더 버튼을 많이 누른 경우
    if move_cnt > cnt:
        break

    # 이전 버튼 중 고장난 버튼이 없었던 경우
    if idx == 0 or move['n']:
        # 고장나지 않은 버튼인 경우
        if int(n) not in trouble:
            for m in move:
                m += n
                print("m", m)
        # 고장난 버튼인 경우
        else:
            # 더 큰 번호 확인
            up = [x for x in range(int(n), 10) if x not in trouble]
            # 더 큰 번호 버튼 존재 경우
            if up:
                move['up'] = move['n'] + up[0]
            # 현재 숫자보다 큰 번호 버튼 없는 경우
            else:
                # 가장 첫번째 번호인 경우
                if idx == 0:
                    move_cnt += 1
                    if normal[0] == 0:
                        move['up'] = f'{normal[1]}{normal[0]}'
                    else:
                        move['up'] = f'{normal[0]}{normal[0]}'
                # 첫번째 번호 아닌 경우
                else:
                    i = idx - 1
                    chk = True
                    temp = move['n']
                    while chk:
                        up = [x for x in range(temp[i] + 1, 10) if x not in trouble]
                        if up:
                            temp[i] = str(up[0])
                            chk = False
                        else:
                            temp[i] = str(normal[0])
                            i -= 1
            print("up", up)

            # ========================================
            # 더 작은 번호 확인
            down = [x for x in range(int(n)) if x in normal]
            print('down', down)

            # 정상인 경우 제거
            move['n'] = None

    # 이전에 이미 고장난 버튼이 존재한 경우
    else:
        move['up'] += str(normal[-1])
        move['down'] += str(normal[0])

    move_cnt += 1
print(move)