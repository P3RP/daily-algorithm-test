'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/06/13
boj.kr/1963
소수 경로

문제 :
소수를 유난히도 좋아하는 창영이는 게임 아이디 비밀번호를 4자리 ‘소수’로 정해놓았다. 어느 날 창영이는 친한 친구와 대화를 나누었는데:

“이제 슬슬 비번 바꿀 때도 됐잖아”
“응 지금은 1033으로 해놨는데... 다음 소수를 무엇으로 할지 고민중이야"
“그럼 8179로 해”
“흠... 생각 좀 해볼게. 이 게임은 좀 이상해서 비밀번호를 한 번에 한 자리 밖에 못 바꾼단 말이야. 예를 들어 내가 첫 자리만 바꾸면 8033이 되니까 소수가 아니잖아. 여러 단계를 거쳐야 만들 수 있을 것 같은데... 예를 들면... 1033 1733 3733 3739 3779 8779 8179처럼 말이야.”
“흠...역시 소수에 미쳤군. 그럼 아예 프로그램을 짜지 그래. 네 자리 소수 두 개를 입력받아서 바꾸는데 몇 단계나 필요한지 계산하게 말야.”
“귀찮아”
그렇다. 그래서 여러분이 이 문제를 풀게 되었다. 입력은 항상 네 자리 소수만(1000 이상) 주어진다고 가정하자. 주어진 두 소수 A에서 B로 바꾸는 과정에서도 항상 네 자리 소수임을 유지해야 하고, ‘네 자리 수’라 하였기 때문에 0039 와 같은 1000 미만의 비밀번호는 허용되지 않는다.

입력 :
첫 줄에 test case의 수 T가 주어진다. 다음 T줄에 걸쳐 각 줄에 1쌍씩 네 자리 소수가 주어진다.

결과 :
각 test case에 대해 두 소수 사이의 변환에 필요한 최소 회수를 출력한다. 불가능한 경우 Impossible을 출력한다.

'''
from copy import deepcopy
import sys
import math
from collections import deque

input = sys.stdin.readline

c = int(input())

arr = [[0 for _ in range(2)] for _ in range(c)]
for i in range(c):
    a, b = input().split()
    arr[i][0], arr[i][1] = int(a), int(b)

# 2로 나누어지는 것은 소수가 아니므로 -1 이 되도록 한다
visit_list = [i%2 - 1 for i in range(10000)]

# prime num list
prime_list = [True for _ in range(10000)]

# 소수를 매번 확인해도 되지만, 9999 까지이기도 하고, 여러번 반복하므로
# 에라토스테네스의 체를 이용하여 소수 리스트를 가지고 있는 것이 효율적이라 판단
for i in range(2, int(math.sqrt(10000))+1):
    if prime_list[i] == True:
        j = 2
        while i*j < 10000:
            prime_list[i*j] = False
            j += 1

def list_to_int(number):
    return int(''.join(str(i) for i in number))

# bfs 로 푸는것이 효율적일 것 같다.
def bfs(start_num, find_num, visit_list):
    # 처음부터 같은게 들어온다면 통과
    if start_num == find_num:
        return 0

    visit_list[start_num] = 1
    queue = deque()
    queue.append(start_num)
    count = 0
    while(1):
        size = len(queue)
        # 더이상 큐에 볼 아이템이 없으면 가능한 소수가 없다는 것
        if(size == 0) :
            return -1
        # 찾았다면 바로 리턴한다. bfs는 찾은 순간이 최소의 순간이기 때문
        elif(visit_list[find_num]):
            return visit_list[find_num]
        else :
            count += 1
            for _ in range(size):
                item = queue.popleft()
                # 첫번째 자리 변경
                first_item_list = [int(i) for i in str(item)]
                for i in range(1,10):
                    first_item_list[0] = i
                    if prime_list[list_to_int(first_item_list)] and visit_list[list_to_int(first_item_list)] == 0:
                        visit_list[list_to_int(first_item_list)] = count
                        queue.append(list_to_int(first_item_list))
                # 두번째 자리 변경
                second_item_list = [int(i) for i in str(item)]
                for i in range(0,10):
                    second_item_list[1] = i
                    if prime_list[list_to_int(second_item_list)] and visit_list[list_to_int(second_item_list)] == 0:
                        visit_list[list_to_int(second_item_list)] = count
                        queue.append(list_to_int(second_item_list))
                # 세번째 자리 변경
                third_item_list = [int(i) for i in str(item)]
                for i in range(0,10):
                    third_item_list[2] = i
                    if prime_list[list_to_int(third_item_list)] and visit_list[list_to_int(third_item_list)] == 0:
                        visit_list[list_to_int(third_item_list)] = count
                        queue.append(list_to_int(third_item_list))
                # 네번째 자리 변경
                fourth_item_list = [int(i) for i in str(item)]
                for i in range(1,10, 2):
                    fourth_item_list[3] = i
                    if prime_list[list_to_int(fourth_item_list)] and visit_list[list_to_int(fourth_item_list)] == 0:
                        visit_list[list_to_int(fourth_item_list)] = count
                        queue.append(list_to_int(fourth_item_list))

    

for i in range(c):
    result = bfs(arr[i][0], arr[i][1], deepcopy(visit_list))
    if result >=0:
        print(result)
    else:
        print("Impossible")

