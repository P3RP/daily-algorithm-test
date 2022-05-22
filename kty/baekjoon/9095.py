'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/05/17
boj.kr/9095
1, 2, 3 더하기

문제 :
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

입력 :
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.
결과 :
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.
'''

import sys
input = sys.stdin.readline

count = int(input())
k = 0


def find_combination(now, n):
    global k
    if now > n:
        return
    if now == n:
        k += 1
        return
    else:
        for i in range(1, 4):
            find_combination(now+i, n)


for _ in range(count):
    n = int(input())
    k = 0
    find_combination(0, n)
    print(k)
