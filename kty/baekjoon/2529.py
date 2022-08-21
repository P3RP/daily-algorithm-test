'''
******* 문제 푼 후 느낀 것 *********
itertools 에 있는 조합을 모두 구해서 풀려고 했다.
이거 매우 안좋은 생각같다.
왜냐하면 저것을 이용하면 모든 경우의 수를 구하게되기 때문이다.
-> 하지만 dfs 를 이용하여 일일이 경우를 계산하면 중간에 안되는 경우가 있기 때문에 이것을 사용하는 것이 더 빠르다.

어떠한 조건에 의해 뽑기를 할때는 효율성을 위해 직접 계산할 수 있도록 하자
itertools를 쓰는 경우는 조건이 없이 무조건 모든 경우를 합쳐서 봐야할때만 사용하자.
'''

'''
2022/08/12
boj.kr/2529
부등호

문제 :
두 종류의 부등호 기호 ‘<’와 ‘>’가 k개 나열된 순서열 A가 있다. 
우리는 이 부등호 기호 앞뒤에 서로 다른 한 자릿수 숫자를 넣어서 모든 부등호 관계를 만족시키려고 한다. 예를 들어, 제시된 부등호 순서열 A가 다음과 같다고 하자. 

A ⇒ < < < > < < > < >
부등호 기호 앞뒤에 넣을 수 있는 숫자는 0부터 9까지의 정수이며 선택된 숫자는 모두 달라야 한다. 아래는 부등호 순서열 A를 만족시키는 한 예이다. 

3 < 4 < 5 < 6 > 1 < 2 < 8 > 7 < 9 > 0

이 상황에서 부등호 기호를 제거한 뒤, 숫자를 모두 붙이면 하나의 수를 만들 수 있는데 이 수를 주어진 부등호 관계를 만족시키는 정수라고 한다. 
그런데 주어진 부등호 관계를 만족하는 정수는 하나 이상 존재한다. 예를 들어 3456128790 뿐만 아니라 5689023174도 아래와 같이 부등호 관계 A를 만족시킨다. 

5 < 6 < 8 < 9 > 0 < 2 < 3 > 1 < 7 > 4

여러분은 제시된 k개의 부등호 순서를 만족하는 (k+1)자리의 정수 중에서 최댓값과 최솟값을 찾아야 한다. 
앞서 설명한 대로 각 부등호의 앞뒤에 들어가는 숫자는 { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }중에서 선택해야 하며 선택된 숫자는 모두 달라야 한다. 

입력 :
첫 줄에 부등호 문자의 개수를 나타내는 정수 k가 주어진다. 그 다음 줄에는 k개의 부등호 기호가 하나의 공백을 두고 한 줄에 모두 제시된다. k의 범위는 2 ≤ k ≤ 9 이다. 

결과 :
여러분은 제시된 부등호 관계를 만족하는 k+1 자리의 최대, 최소 정수를 첫째 줄과 둘째 줄에 각각 출력해야 한다. 
단 아래 예(1)과 같이 첫 자리가 0인 경우도 정수에 포함되어야 한다. 모든 입력에 답은 항상 존재하며 출력 정수는 하나의 문자열이 되도록 해야 한다. 
'''
import sys

def compare(a, b, sign):
    if sign == '<' :
        return a < b
    else :
        return a > b

input = sys.stdin.readline

compare_count = int(input())
sign_list = list(map(str, input().split()))

min_value = ''
max_value = ''


def dfs(number_string, visited = [0 for _ in range(10)]):
    global min_value
    global max_value
    if len(number_string) > compare_count:
        if min_value == '':
            min_value = number_string
        else :
            max_value = number_string
        return
    

    for i in range(10):
        if not visited[i] :
            if len(number_string) == 0 or compare(number_string[-1], str(i), sign_list[len(number_string)-1]):
                visited[i] = 1
                dfs(number_string+str(i), visited)
                visited[i] = 0


dfs("")
print(max_value)
print(min_value)
        
