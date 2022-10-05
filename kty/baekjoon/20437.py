'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/09/26
boj.kr/20437
문자열 게임2
'''

import sys
input = sys.stdin.readline

def solution(W, K):
    alpha_dict = dict()
    for c in range(ord('a'), ord('z')+1):
        alpha_dict[chr(c)] = []

    W = W.strip()
    # 2개를 동시에 체크한다.
    # k 개 포함하면 문자열을 줄이고,
    for idx, c in enumerate(W):
        alpha_dict[c].append(idx)
    
    max_len = -1
    min_len = sys.maxsize

    for value in alpha_dict.values():
        for i in range(len(value)-K+1):
            max_len = max(value[i+K-1] - value[i] + 1, max_len)
            min_len = min(value[i+K-1] - value[i] + 1, min_len)
    

    if max_len == -1:
        print(-1)
    else :
        print(min_len, max_len)

T = int(input())

for _ in range(T):
    W = input()
    K = int(input())
    solution(W, K)