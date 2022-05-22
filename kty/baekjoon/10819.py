'''
******* 문제 푼 후 느낀 것 *********
순열을 어떻게 구현하는지 몰라 dfs로 순열을 구하는 방법을 찾아보았다.
순열에서는 모든 경우를 볼 수 있어야 하기 때문에 뽑았던 것을 다시 돌려놓도록 한다.
'''

'''
2022/05/22
boj.kr/10819
차이를 최대로

문제 :
N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.

|A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

입력 :
첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다. 둘째 줄에는 배열 A에 들어있는 정수가 주어진다. 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.

결과 :
첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력한다.
'''

import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

max_result = -999999999

visited = [False for _ in range(n)]
select_arr = []


def dfs(c):
    global max_result
    if c == n:
        result = 0
        for i in range(n-1):
            result = result + abs(select_arr[i+1] - select_arr[i])
        max_result = max(max_result, result)
        return
    else:
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                select_arr.append(arr[i])
                dfs(c+1)
                # 선택했던 것을 다시 원래대로 돌려서 순서를 다르게 뽑을 수 있게 한다 .
                visited[i] = False
                select_arr.pop()


dfs(0)
print(max_result)

# 문제를 잘못읽고
# |A[0] - A[1]| + |A[2] - A[3]| + ... + |A[N-2] - A[N-1]|
# 이렇게 가는줄 알고 풀었던 방식
# 2개식 짝지어서 하는 줄 알았다.
# 문제 잘 읽기
'''
import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

negative_arr = []
positive_arr = []

for i in range(n):
    if arr[i] < 0:
        negative_arr.append(arr[i])
    else:
        positive_arr.append(arr[i])


positive_arr = sorted(positive_arr, reverse=True)  # 10, 5,4,3,2,1 ...
negative_arr = sorted(negative_arr)  # -10, -9 ...

len_positive_arr = len(positive_arr)
len_negative_arr = len(negative_arr)

print(positive_arr)

result = 0
if len_positive_arr == len_negative_arr:
    for i in range(len_negative_arr):
        result += positive_arr[i]
        result -= negative_arr[i]

elif len_positive_arr > len_negative_arr:
    for i in range(len_negative_arr):
        result += positive_arr[i]
        result -= negative_arr[i]

    remain = len_positive_arr - len_negative_arr
    for i in range(len_negative_arr, remain//2):
        result += positive_arr[i]
    for i in range(len_negative_arr+(remain//2), len_positive_arr):
        result -= positive_arr[i]

else:
    for i in range(len_positive_arr):
        result += positive_arr[i]
        result -= negative_arr[i]

    remain = len_negative_arr - len_positive_arr

    for i in range(len_positive_arr, remain//2):
        result -= negative_arr[i]
    for i in range(len_positive_arr+(remain//2), len_negative_arr):
        result += negative_arr[i]

print(result)
'''
