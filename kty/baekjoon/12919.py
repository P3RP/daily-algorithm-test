'''
******* 문제 푼 후 느낀 것 *********
처음에는 S에서 문제 그대로 문자를 추가하면서 풀어나갔었다.
그 경우 모든 경우에 대해 탐색해야하기 떄문에 시간이 오래걸렸다.
반대로 T에서 제거하면서 온다면, 불가능한 경우들을 제외하고 탐색이 가능하다.
예로 ABB 가 있다면 맨 뒤가 A 가 아니기 때문에 해당 경우는 제외할 수 있다.
'''

'''
2022/09/01
boj.kr/12919
A와 B 2

문제 :
수빈이는 A와 B로만 이루어진 영어 단어 존재한다는 사실에 놀랐다. 대표적인 예로 AB (Abdominal의 약자), BAA (양의 울음 소리), AA (용암의 종류), ABBA (스웨덴 팝 그룹)이 있다.

이런 사실에 놀란 수빈이는 간단한 게임을 만들기로 했다. 두 문자열 S와 T가 주어졌을 때, S를 T로 바꾸는 게임이다. 문자열을 바꿀 때는 다음과 같은 두 가지 연산만 가능하다.

문자열의 뒤에 A를 추가한다.
문자열의 뒤에 B를 추가하고 문자열을 뒤집는다.
주어진 조건을 이용해서 S를 T로 만들 수 있는지 없는지 알아내는 프로그램을 작성하시오. 

입력 :
첫째 줄에 S가 둘째 줄에 T가 주어진다. (1 ≤ S의 길이 ≤ 49, 2 ≤ T의 길이 ≤ 50, S의 길이 < T의 길이)

결과 :
S를 T로 바꿀 수 있으면 1을 없으면 0을 출력한다
'''
import sys
input = sys.stdin.readline

S = list(input().strip())
T = list(input().strip())

find = 0
def dfs(T):
    global S
    global find
    if find :
        return 
    
    if len(S) == len(T):
        if S == T:
            find = 1
            return
        return
    
    if T[(len(T)-1)]=='A':
        dfs(T[:-1])
    if T[0] == 'B':
        dfs(list(reversed(T[1:])))


dfs(T)
print(find)


