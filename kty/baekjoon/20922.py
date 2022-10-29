'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/10/14
boj.kr/20922
겹치는 건 싫어
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

count_dict = dict()

num_list = list(map(int, input().split()))

start = 0
end = 0

count_dict[num_list[0]] = 1
max_len = 1

while(1):

    if start > end or end >= N-1:
        break

    if start - end + 1  < max_len :
        end += 1
        if num_list[end] in count_dict:
            count_dict[num_list[end]] += 1
        else :
            count_dict[num_list[end]] = 1
    is_over = False
    for value in count_dict.values():
        if value > K :
            is_over = True
            break
    
    if not is_over:
        max_len = max(end - start + 1, max_len)
        end += 1
        if num_list[end] in count_dict:
            count_dict[num_list[end]] += 1
        else :
            count_dict[num_list[end]] = 1
    else :
        if num_list[start] in count_dict:
            count_dict[num_list[start]] -= 1
            if count_dict[num_list[start]] == 0:
                del count_dict[num_list[start]]
        else :
            count_dict[num_list[end]] = 1
        start += 1

print(max_len)