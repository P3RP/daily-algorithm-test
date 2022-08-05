'''
******* 문제 푼 후 느낀 것 *********
문제를 읽고, 생각먼저 하는 것이 무조건 필요하다.
바로 문제를 풀려하지 말고, 종이에 적으면서 확인하자.

본 문제의 경우는 감소하는 수가 되기 위해서는 앞의 자리 수보다 뒤의 자리 수가 반드시 작아야 했다. 
이것을 고려하지 못하고 처음에는 dp 처럼 풀려고 했었다... 9876543210 배열을 만들고, 어떤수가 감소하는 수인지 저장하고,
해당 패턴을 가지고 있는 것들에 대해서 메모이제이션 하면서 count 하려고 했었다... 아직도 많이 부족한 것 같다. 더 풀어보자.
'''

'''
2022/08/1
boj.kr/1038
감소하는 수

문제 :
음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면, 그 수를 감소하는 수라고 한다. 예를 들어, 321과 950은 감소하는 수지만, 322와 958은 아니다. N번째 감소하는 수를 출력하는 프로그램을 작성하시오. 0은 0번째 감소하는 수이고, 1은 1번째 감소하는 수이다. 만약 N번째 감소하는 수가 없다면 -1을 출력한다.

입력 :
첫째 줄에 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수 또는 0이다.

결과 :
첫째 줄에 N번째 감소하는 수를 출력한다.
'''

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

count = -1

queue = deque()
for i in range(0, 10):
    queue.append(i)
    

find = False
while(queue):
    item = queue.popleft()
    count += 1
    
    if count == N:
        print(item)
        find = True
        break
    else :
        for i in range(10):
            if item % 10 > i:
                queue.append((item*10)+i)

if not find :
    print(-1)
            

