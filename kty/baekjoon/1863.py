'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/10/17
boj.kr/1863
스카이라인 쉬운거
'''
import sys

input = sys.stdin.readline

N = int(input())

# 작은 것이 나오면 pop 한다. 이때 작은 것 보다 작은 것이 나오기 전까지 pop 하고 마지막에 push 해준다.
# 큰것이 나오면 push 한다.
# 증가하는 경우는 0 이 나오게 되면 set을 초기화하고, 해당 높이가 set에 들어있지 않은 경우 해준다.
change_list = []
for _ in range(N):
    x, y = map(int ,input().split())
    change_list.append((x,y))

change_list.sort()

height_stack = []
count = 0
for i in range(N):
    pos, height = change_list[i]


    # 0 이 되면 처음부터 다시 세야한다.
    if height == 0:
        height_stack = []

    else:
        while(1):
            if len(height_stack) == 0:
                height_stack.append(height)
                count += 1
                break
        
            top_height = height_stack[len(height_stack)-1]
            if top_height == height:
                break
            elif top_height > height:
                height_stack.pop()
            else :
                height_stack.append(height)
                count += 1
                break

print(count)