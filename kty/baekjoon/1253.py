'''
******* 문제 푼 후 느낀 것 *********
흠!
투포인터로 풀었다!
'''

'''
2022/08/27
boj.kr/1253
좋다

문제 :
N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 “좋다(GOOD)”고 한다.

N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라.

수의 위치가 다르면 값이 같아도 다른 수이다.

입력 :
첫째 줄에는 수의 개수 N(1 ≤ N ≤ 2,000), 두 번째 줄에는 i번째 수를 나타내는 Ai가 N개 주어진다. (|Ai| ≤ 1,000,000,000, Ai는 정수)

결과 :
좋은 수의 개수를 첫 번째 줄에 출력한다.
'''
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

A = sorted(A)

count = 0

for i in range(0, N):
    start = 0
    end = N-1
    if start == i:
        start += 1
    if end == i :
        end -= 1
    while(start < end) :
        value = A[start] + A[end]

        if value == A[i]:
            count += 1
            break
        if value < A[i]:
            start += 1
        elif value > A[i]:
            end -= 1
        if start == i:
            start += 1
        if end == i :
            end -= 1

print(count)


