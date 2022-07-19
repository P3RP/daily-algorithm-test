'''
******* 문제 푼 후 느낀 것 *********
시관초과를 해결하지 못해 pypy3 으로 통과하게되었다.
python3 풀이를 보니, 문자열로 계산하게되면 시간이 오래걸려 bit 연산 또는, 리스트에 알파벳을 넣고 계산하는 풀이들이 많았다.
알파벳과 관련된 문제가 나오면 비트연산 또는 26길이의 리스트를 만들어 그것으로 해결해도록 해보자
'''

'''
2022/07/18
boj.kr/1062
가르침

문제 :
남극에 사는 김지민 선생님은 학생들이 되도록이면 많은 단어를 읽을 수 있도록 하려고 한다. 그러나 지구온난화로 인해 얼음이 녹아서 곧 학교가 무너지기 때문에, 
김지민은 K개의 글자를 가르칠 시간 밖에 없다. 김지민이 가르치고 난 후에는, 학생들은 그 K개의 글자로만 이루어진 단어만을 읽을 수 있다. 

김지민은 어떤 K개의 글자를 가르쳐야 학생들이 읽을 수 있는 단어의 개수가 최대가 되는지 고민에 빠졌다.

남극언어의 모든 단어는 "anta"로 시작되고, "tica"로 끝난다. 남극언어에 단어는 N개 밖에 없다고 가정한다. 학생들이 읽을 수 있는 단어의 최댓값을 구하는 프로그램을 작성하시오.

입력 :
첫째 줄에 단어의 개수 N과 K가 주어진다. N은 50보다 작거나 같은 자연수이고, K는 26보다 작거나 같은 자연수 또는 0이다. 
둘째 줄부터 N개의 줄에 남극 언어의 단어가 주어진다. 단어는 영어 소문자로만 이루어져 있고, 길이가 8보다 크거나 같고, 15보다 작거나 같다. 모든 단어는 중복되지 않는다.

결과 :
첫째 줄에 김지민이 K개의 글자를 가르칠 때, 학생들이 읽을 수 있는 단어 개수의 최댓값을 출력한다.
'''
import sys
input = sys.stdin.readline

def can_read(word, alpha) :
    for i in word:
        if i not in alpha:
            return 0
    return 1

def dfs(max_len, start=0, visited=[]):
    global need_alpha_list
    global alphas_in_word_list
    global max_count
    global alpha_combi

    if len(alpha_combi) == max_len or len(alpha_combi) == len(need_alpha_list):
        # 여기서 가능한 단어가 몇개인지 찾는다.
        count = 0
        for alphas in alphas_in_word_list:
            count += can_read(alphas, alpha_combi)
        max_count = max(count, max_count)
        return

    else :
        for i in range(start, len(need_alpha_list)):
            if visited[i] != 1:
                visited[i] = 1
                alpha_combi.append(need_alpha_list[i])
                dfs(max_len=max_len, start= i+1, visited=visited)
                alpha_combi.pop()
                visited[i] = 0
    
    


def get_alpha_set(word) :
    # 문자열에는 공백문자가 들어있으므로 빼준다
    essential_alpha_list = ['a', 'c', 'n', 't','i', '\n']
    word_set = list(set(word) - set(essential_alpha_list))
    return word_set

word_count, alpha_count = map(int, input().split())
word_list = []

for _ in range(word_count):
    word = list(input())
    word_list.append(word[4:-4])

if alpha_count < 5 :
    print(0)
else :
    alphas_in_word_list = []
    need_alpha_list = []
    for word in word_list:
        alpha_set = get_alpha_set(word)
        alphas_in_word_list.append(alpha_set)

    for word in alphas_in_word_list:
        need_alpha_list = need_alpha_list + list(word)
    

    need_alpha_list = list(set(need_alpha_list))

    max_count = 0
    visited = [0 for _ in range(len(need_alpha_list))]
    alpha_combi = []
    dfs(alpha_count-5, 0, visited)
    
    print(max_count)
    

