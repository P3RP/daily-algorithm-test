'''
******* 문제 푼 후 느낀 것 *********
KMP 라는 알고리즘을 처음 들어보았다. 무척 어려웠다.
이거는 암기가 필요할 것 같다. getTable을 만드는 것을 꼭 암기할 수 있도록 하자.
'''

'''
2022/07/26
boj.kr/16916
부분 문자열

문제 :
문자열 S의 부분 문자열이란, 문자열의 연속된 일부를 의미한다.
예를 들어, "aek", "joo", "ekj"는 "baekjoon"의 부분 문자열이고, "bak", "p", "oone"는 부분 문자열이 아니다.
문자열 S와 P가 주어졌을 때, P가 S의 부분 문자열인지 아닌지 알아보자.

입력 :
첫째 줄에 문자열 S, 둘째 줄에 문자열 P가 주어진다. 두 문자열은 빈 문자열이 아니며, 
길이는 100만을 넘지 않는다. 또, 알파벳 소문자로만 이루어져 있다.

결과 :
P가 S의 부분 문자열이면 1, 아니면 0을 출력한다.
'''
import sys
input = sys.stdin.readline

S = list(input().strip())
P = list(input().strip())

def getTable(pattern) :
    p_len = len(pattern)
    table = [0 for _ in range(p_len)]
    j = 0
    for i in range(1, p_len):
        # j가 올라가있고, 테이블 값이 사로 다르면 j 를 아래로 내린다.
        # 즉, 일치하는 문자가 줄어드는 것이다. 
        while(j > 0 and pattern[i] != pattern[j]) :
            j = table[j-1]
        # 그렇게해서 일치하게 만들어 놓았다면, 
        # 몇개가 일치하는지 구한다
        if(pattern[i] == pattern[j]):
            table[i] = j + 1
            j = j + 1
    return table

table = getTable(P)

j = 0
find = False
for i in range(len(S)):
    while(j>0 and P[j] != S[i]):
        j = table[j-1]

    if(P[j] == S[i]):
        j += 1
    if(j == len(P)):
        find = True
        break

if find :
    print(1)
else :
    print(0)
