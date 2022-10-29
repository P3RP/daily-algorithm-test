'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/10/12
boj.kr/11501
주식
'''
import sys

for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    price_list = list(map(int, sys.stdin.readline().split()))

    max_price = price_list[-1]
    answer = 0
    for i in range(N-2, -1, -1):
        if price_list[i] > max_price:
            max_price = price_list[i]
        else :
            answer += max_price - price_list[i]
    print(answer)