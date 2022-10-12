'''
******* 문제 푼 후 느낀 것 *********
나도 햄버거 먹고싶당...
'''

'''
2022/10/12
boj.kr/19941
햄버거 분배
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

pos_list = list(input())

now_pos = 0
count = 0
for now_pos in range(N):

    if pos_list[now_pos] == 'P':
        start = 0 if now_pos - K < 0 else now_pos - K
        end = now_pos + K if now_pos + K < N else N-1

        for i in range(start, end+1):
            if pos_list[i] == 'H':
                pos_list[i] = "N"
                count += 1
                break

print(count)