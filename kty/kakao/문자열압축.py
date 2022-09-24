'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/09/24
https://school.programmers.co.kr/learn/courses/30/lessons/60057
문자열 압축
'''

def solution(t):
    answer = len(t)

    for i in range(1, len(t)//2 + 1):
        s = t[:]
        idx = 0
        
        before = ""
        result = ""
        count = 0
        while(idx+i < len(t)+1):

            c = s[idx:idx+i]
            # 이전과 패턴이 다르다면 이전에 있던 것을 추가하고 
            # 새롭게 패턴을 설정한다.
            if before != c:
                if count > 1 :
                    result += str(count) + before
                else :
                    result += before
                before = c
                count = 1
            # 패턴이 동일한 경우
            # 숫자를 증가시켜준다
            else :
                if before == "":
                    before = c
                count += 1
            # 패턴 길이만큼 증가
            idx += i 
        
        # 이후 나오고 나서 count가 남아있는 데 추가되지 못한 것이 있을 수 있다.
        if count > 1 :
            result += str(count) + before
        else :
            result += before

        if idx < len(s):
            result += s[idx:]
        answer = min(answer, len(result))
    return answer

print(solution("aabbaccc"))
