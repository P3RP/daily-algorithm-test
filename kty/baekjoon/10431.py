'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/10/14
boj.kr/10431
줄세우기
'''
import sys
input = sys.stdin.readline

P = int(input())

for _ in range(P):
    input_list = list(map(int, input().split()))
    case_num = input_list[0]
    height_list = input_list[1:]
    move = 0
    sort_height_list = []
    for i in range(20):
        j = 0
        for _ in range(len(sort_height_list)):
            if sort_height_list[j] > height_list[i]:
                break
            j += 1
        move += len(sort_height_list) - j
        sort_height_list.insert(j, height_list[i])
    
    print(case_num , move)