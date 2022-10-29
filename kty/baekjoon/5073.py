'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/10/21
boj.kr/5073
삼각형과 세 변
'''
import sys
input = sys.stdin.readline

while(1):
    length_list = sorted(list(map(int, input().split())))

    first, second, third = length_list

    if first == 0 and second == 0 and third == 0:
        break

    if first == second == third :
        print("Equilateral")
    else:
        if first + second <= third:
            print("Invalid")
        elif first == second or second == third or first == third:
            print("Isosceles")
        else:
            print("Scalene")
