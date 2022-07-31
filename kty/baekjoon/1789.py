'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/07/31
boj.kr/1789
수들의 합

문제 :
서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

입력 :
첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.

결과 :
첫째 줄에 자연수 N의 최댓값을 출력한다.
'''
import sys
input = sys.stdin.readline

N = int(input())

idx = 1
while(1):
    check_value = ((idx+1)*idx)//2
    if check_value == N:
        print(idx)
        break

    elif check_value > N :
        print(idx-1)
        break
    idx += 1