'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/05/16
boj.kr/1107
리모컨

수빈이는 TV를 보고 있다. 수빈이는 채널을 돌리려고 했지만, 버튼을 너무 세게 누르는 바람에, 일부 숫자 버튼이 고장났다.

리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다. +를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고, -를 누르면 -1된 채널로 이동한다. 
채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.

수빈이가 지금 이동하려고 하는 채널은 N이다. 어떤 버튼이 고장났는지 주어졌을 때, 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오. 

수빈이가 지금 보고 있는 채널은 100번이다.

입력 :
첫째 줄에 수빈이가 이동하려고 하는 채널 N (0 ≤ N ≤ 500,000)이 주어진다.  둘째 줄에는 고장난 버튼의 개수 M (0 ≤ M ≤ 10)이 주어진다. 
고장난 버튼이 있는 경우에는 셋째 줄에는 고장난 버튼이 주어지며, 같은 버튼이 여러 번 주어지는 경우는 없다.
결과 :
첫째 줄에 채널 N으로 이동하기 위해 버튼을 최소 몇 번 눌러야 하는지를 출력한다.
'''

import sys
input = sys.stdin.readline

move_to = str(input())
broken_count = int(input())
broken_list = []
if broken_count:
    broken_list = list(map(int, input().split()))

start = 100
move_count = 0
min_move_count = abs(int(move_to)-start)


# 그렇지 않은 경우 모든 버튼을 눌러보면서 확인한다.
# 이때 1000001 로 한 이유는 500,000 안의 채널로 이동하지만, 채널은 사실상 무한이고, 더 큰 채널에서 500,000 으로 오는것이 더 빠른 경우가 있을 수 있으므로
# 10000001 로 설정
for i in range(1000001):
    num = str(i)
    broken_check = False
    for c in num:
        if int(c) in broken_list:
            broken_check = True
            break
    if not broken_check:
        min_move_count = min(min_move_count, abs(
            int(num)-int(move_to)) + len(num))
print(min_move_count)
