'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/10/07
boj.kr/20920
영단어 암기는 괴로워
'''
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

# (횟수, 길이, 첫문자)
word_dict = dict()

for _ in range(N):
    word = input().strip()
    word_len = len(word)
    
    if word_len < M :
        continue

    if word not in word_dict:
       word_dict[word] = (-1, -word_len, word) 
    else :
        a, b, c = word_dict[word]
        word_dict[word] = (a-1, b, c)

for key in sorted(word_dict.items(), key=lambda x: (x[1][0], x[1][1], x[1][2])):
    print(key[0])