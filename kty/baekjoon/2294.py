'''
******* 문제 푼 후 느낀 것 *********
동전1 (boj.kr/2293) 을 풀고 난 이후 풀어서 쉽게 풀 수 있었던 것 같다.
다음에는 랜덤하게 dp 문제가 나와도 잘 풀 수 있도록 노력하자.
'''

'''
2022/08/1
boj.kr/2294
동전 2

문제 :
n가지 종류의 동전이 있다. 이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그러면서 동전의 개수가 최소가 되도록 하려고 한다. 각각의 동전은 몇 개라도 사용할 수 있다.

사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

입력 :
첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 동전의 가치는 100,000보다 작거나 같은 자연수이다. 가치가 같은 동전이 여러 번 주어질 수도 있다.

결과 :
첫째 줄에 사용한 동전의 최소 개수를 출력한다. 불가능한 경우에는 -1을 출력한다.
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coin_list = []

for _ in range(n):
    coin_list.append(int(input()))

dp = [0] + [sys.maxsize for _ in range(k)]

for coin in coin_list:
    for j in range(coin, k+1):
        dp[j] = min(dp[j-coin]+1, dp[j])

if dp[k] == sys.maxsize:
    print(-1)
else :
    print(dp[k])