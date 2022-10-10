'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/10/10
boj.kr/2512
예산
'''
import sys
input = sys.stdin.readline

N = int(input())

money_list = list(map(int, input().split()))
max_money = int(input())

if sum(money_list) <= max_money :
    print(max(money_list))

else :

    start = 0
    end = max_money
    answer = 0
    while(start <= end):
        mid = (start + end) // 2
        cheking_money = max_money
        for money in money_list:
            if cheking_money < 0:
                break

            # 주어진 상한가보다 크다면
            if money > mid:
                # mid만 뺀다
                cheking_money -= mid
            # 그렇지 않다면 할당된 예산만 뺸다.
            else :
                cheking_money -= money
        if cheking_money < 0:
            end = mid - 1
        else :
            answer = mid
            start = mid + 1

    print(answer)
