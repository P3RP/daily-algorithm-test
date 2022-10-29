'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/10/19
boj.kr/4949
균형잡힌 세상
'''
import sys
input = sys.stdin.readline

while(1):
    check_string = input().rstrip()
    my_stack = []
    if check_string == ".":
        break
    
    for c in check_string:
        if c == "(":
            my_stack.append("(")
        elif c == "[":
            my_stack.append("[")
        
        elif c==")" or c == ']':
            if len(my_stack) == 0:
                my_stack.append(c)
                break
            elif c == ")":
                if my_stack[len(my_stack)-1] == "(":
                    my_stack.pop()
                else :
                    break
            
            elif c == "]":
                if my_stack[len(my_stack)-1] == "[":
                    my_stack.pop()
                else :
                    break
    if len(my_stack) == 0:
        print("yes")
    else :
        print('no')