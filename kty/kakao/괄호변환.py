'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/09/24
https://school.programmers.co.kr/learn/courses/30/lessons/60058
괄호변환
'''

from copy import deepcopy
def solution(p):

    if len(p) == 0 :
        return p
    # 2개의 문자열로 나눈다.
    left_count = 0
    right_count = 0

    for i in range(len(p)):
        if p[i] == '(':
            left_count +=1
        else :
            right_count += 1
        if left_count == right_count :
            break
    
    u = p[:left_count+right_count]
    v = p[left_count+right_count:]
    print(u, check_correct(u))
    if not check_correct(u):
        new_v = "(" + solution(v)
        new_v += ")"
        u = u[1:-1]
        for i in range(len(u)):
            if u[i] == ')':
                u = u[:i] + '(' + u[i+1:]
            else :
                u = u[:i] + ')' + u[i+1:]
        return new_v + u
    else :
        u += solution(v)
        return u




def check_correct(w):
    w = list(reversed(w))
    check_stack = []
    while(w):
        c = w.pop()
        if len(check_stack) == 0:
            check_stack.append(c)
        else :
            last_c = check_stack[len(check_stack)-1]
            if last_c == ')':
                check_stack.append(c)
            else :
                if last_c == '(':
                    if c == ')':
                        check_stack.pop()
                    else :
                        check_stack.append(c)
    
    if len(check_stack) == 0:
        return True
    return False


print(solution("()))((()"))

    

    # 올바른 문자열 이라면 다른 문자열을 검사한다.
    # 올바른 문자열이 아니라면 다시 재귀문을 반복한다.