'''
******* 문제 푼 후 느낀 것 *********
처음에 combination 으로 접근했더니 시간초과가 발생했다.
작성하면서도 for 중첩이 너무 많아 시간초과가 날 것 같긴 했지만 일단 테스트케이스는 통과해서 채점을 해봤는데 역시나였다.

자꾸 최근 모든 것을 탐색하는 경우에 관련된 문제들만 풀다보니 그런쪽으로 생각이 기울어버린것같다...

문제를 꼼꼼히 읽고, 신중하게 생각 또 생각 하는 습관을 기를 수 있도록 하자. 
'''

'''
2022/07/28
boj.kr/1141
접두사

문제 :
접두사X 집합이란 집합의 어떤 한 단어가, 다른 단어의 접두어가 되지 않는 집합이다. 
예를 들어, {hello}, {hello, goodbye, giant, hi}, 비어있는 집합은 모두 접두사X 집합이다. 
하지만, {hello, hell}, {giant, gig, g}는 접두사X 집합이 아니다.

단어 N개로 이루어진 집합이 주어질 때, 접두사X 집합인 부분집합의 최대 크기를 출력하시오.

입력 :
첫째 줄에 단어의 개수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 단어가 주어진다. 
단어는 알파벳 소문자로만 이루어져 있고, 길이는 최대 50이다. 집합에는 같은 단어가 두 번 이상 있을 수 있다.

결과 :
첫째 줄에 문제의 정답을 출력한다.
'''
import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())

word_list = []

for _ in range(N):
    word_list.append(input().strip())

word_list.sort(key=lambda x: len(x))

result = N

for i in range(N):
    for j in range(i+1, N):
        if word_list[j].find(word_list[i]) == 0 :
            result -= 1
            break
print(result)

