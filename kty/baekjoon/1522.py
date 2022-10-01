'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/10/01
boj.kr/1522
문자열 교환
'''

import sys
input = sys.stdin.readline

ab_string = list(input().strip())

front = 0
while (ab_string[front] != "a"):
    front += 1
back = len(ab_string) - 1

if ab_string[back] == 'a' and front == 0:
    back -= 1

while (ab_string[back] == "b"):
    back -= 1
    
count = 0
while(front < back) :
    while (ab_string[front] == "a"):
        front += 1
    while (ab_string[back] == "b"):
        back -= 1
    
    if front >= back :
        break
    ab_string[front] = 'a'
    ab_string[back] = 'b'
    front += 1
    back -=1
    count += 1

print(count)



