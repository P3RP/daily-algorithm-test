'''
******* 문제 푼 후 느낀 것 *********
생각해내기 어려웠다. 
단순히 bfs로 모든 경우를 탐색한 경우 파이썬으로는 10개의 알파벳이 쓰이면 계산이 불가능했다.

결국 방법을 찾지 못하고 인터넷 검색을 하게 되었다.
인터넷에서는 모든 경우를 탐색하는 방법이 아닌, 공식을 사용해서 풀고 있었다...
더욱 발전할 수 있도록 노력하자.
'''

'''
2022/08/14
boj.kr/1139
단어수학

문제 :
민식이는 수학학원에서 단어 수학 문제를 푸는 숙제를 받았다.
단어 수학 문제는 N개의 단어로 이루어져 있으며, 각 단어는 알파벳 대문자로만 이루어져 있다. 

이때, 각 알파벳 대문자를 0부터 9까지의 숫자 중 하나로 바꿔서 N개의 수를 합하는 문제이다. 같은 알파벳은 같은 숫자로 바꿔야 하며, 두 개 이상의 알파벳이 같은 숫자로 바뀌어지면 안 된다.
예를 들어, GCF + ACDEB를 계산한다고 할 때, A = 9, B = 4, C = 8, D = 6, E = 5, F = 3, G = 7로 결정한다면, 두 수의 합은 99437이 되어서 최대가 될 것이다.
N개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램을 작성하시오.

입력 :
첫째 줄에 단어의 개수 N(1 ≤ N ≤ 10)이 주어진다. 둘째 줄부터 N개의 줄에 단어가 한 줄에 하나씩 주어진다. 
단어는 알파벳 대문자로만 이루어져있다. 모든 단어에 포함되어 있는 알파벳은 최대 10개이고, 수의 최대 길이는 8이다. 서로 다른 문자는 서로 다른 숫자를 나타낸다.

결과 :
첫째 줄에 주어진 단어의 합의 최댓값을 출력한다.
'''
import sys
input = sys.stdin.readline

word_count = int(input())
word_list = []
alpha_dict = dict()
for _ in range(word_count):
    word = input().strip()
    for i in range(len(word)):
        if(word[i] in  alpha_dict):
            alpha_dict[word[i]] += 10**(len(word)-1-i)
        else:
            alpha_dict[word[i]] =  10**(len(word)-1-i)

sorted_dict = sorted(alpha_dict, key=lambda x:-alpha_dict[x])
result = 0
for i in range(9, 9-len(alpha_dict), -1):
    result += alpha_dict[sorted_dict[9-i]]*i
    
print(result)