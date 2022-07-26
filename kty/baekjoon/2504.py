'''
******* 문제 푼 후 느낀 것 *********
이거 나중에 꼭 다시해보기
너무 어렵다
'''

'''
2022/07/17
boj.kr/2504
괄호의 값

문제 :
4개의 기호 ‘(’, ‘)’, ‘[’, ‘]’를 이용해서 만들어지는 괄호열 중에서 올바른 괄호열이란 다음과 같이 정의된다.

한 쌍의 괄호로만 이루어진 ‘()’와 ‘[]’는 올바른 괄호열이다. 
만일 X가 올바른 괄호열이면 ‘(X)’이나 ‘[X]’도 모두 올바른 괄호열이 된다. 
X와 Y 모두 올바른 괄호열이라면 이들을 결합한 XY도 올바른 괄호열이 된다.
예를 들어 ‘(()[[]])’나 ‘(())[][]’ 는 올바른 괄호열이지만 ‘([)]’ 나 ‘(()()[]’ 은 모두 올바른 괄호열이 아니다. 
우리는 어떤 올바른 괄호열 X에 대하여 그 괄호열의 값(괄호값)을 아래와 같이 정의하고 값(X)로 표시한다. 

‘()’ 인 괄호열의 값은 2이다.
‘[]’ 인 괄호열의 값은 3이다.
‘(X)’ 의 괄호값은 2x값(X) 으로 계산된다.
‘[X]’ 의 괄호값은 3x값(X) 으로 계산된다.
올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.
예를 들어 ‘(()[[]])([])’ 의 괄호값을 구해보자. ‘()[[]]’ 의 괄호값이 2 + 3x3=11 이므로 ‘(()[[]])’의 괄호값은 2x11=22 이다. 
그리고 ‘([])’의 값은 2x3=6 이므로 전체 괄호열의 값은 22 + 6 = 28 이다.

여러분이 풀어야 할 문제는 주어진 괄호열을 읽고 그 괄호값을 앞에서 정의한대로 계산하여 출력하는 것이다. 

입력 :
첫째 줄에 괄호열을 나타내는 문자열(스트링)이 주어진다. 단 그 길이는 1 이상, 30 이하이다.

결과 :
첫째 줄에 그 괄호열의 값을 나타내는 정수를 출력한다. 만일 입력이 올바르지 못한 괄호열이면 반드시 0을 출력해야 한다. 

'''
import sys

input = sys.stdin.readline
is_error = False
input_arr = input()
answer = 0
brace_stack = []
for i in range(len(input_arr)-1):
    if input_arr[i] in ['(' , '[' ]:
        brace_stack.append(input_arr[i])
    else :
        temp_sum = 0
        item = ''
        if('(' not in brace_stack and '[' not in brace_stack):
            is_error = True
            break

        if input_arr[i] == ']':
            while(1):
                item = brace_stack.pop()
                if(type(item) == int):
                    temp_sum += item
                else :
                    break
            if (item == '[') :
                if(temp_sum != 0):
                    brace_stack.append(temp_sum * 3)
                else :
                    brace_stack.append(3)
            else : 
                is_error = True
                break
        elif input_arr[i] == ')':
            while(1):
                item = brace_stack.pop()
                if(type(item) == int):
                    temp_sum += item
                else :
                    break
            if (item == '(') :
                if(temp_sum != 0):
                    brace_stack.append(temp_sum * 2)

                else :
                    brace_stack.append(2)
            else : 
                is_error = True
                break



if (is_error) :
    print(0)

else :
    check = False
    for i in ['(', '[', ']', ')'] :
        if i in brace_stack:
            check = True
            print(0)
            break
    if (not check):
        print(sum(brace_stack))