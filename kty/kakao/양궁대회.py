'''
******* 문제 푼 후 느낀 것 *********
비교문을 잘못해서 테스트케이스 2개가 걸렸다.
어떤 것을 비교할때 탈출하는 시점을 잘 찾아야 할 것 같다.

여기서는 낮은 점수부터 화살을 비교하는데, 한번의 비교로 두개다 0이 아니라면
바로 값을 리턴해줬어야 했는데, 이것을 잘 못했다.
'''

'''
2022/09/23
https://school.programmers.co.kr/learn/courses/30/lessons/92342
양궁대회
'''
from copy import deepcopy


def solution(n, info):
    # 해당 칸에 가장 많이 쏜 사람이 해당 점수를 가져감
    # 동일하게 맞춘 경우 누구도 점수를 가져가지 않음
    # 최종 점수가 같으면 어피치가 우승
    global max_value
    answer = [0 for _ in range(11)]
    lion = [0 for _ in range(11)]
    dfs(info, lion, 0, n, answer)
    if answer == [0 for _ in range(11)] or max_value == 0:
        return [-1]
    return answer

def calc_score(apeach, lion) :
    lion_score = 0
    apeach_score = 0
    for i in range(11):
        if apeach[i] == 0 and lion[i] == 0 :
            continue
        if apeach[i] >= lion[i]:
            apeach_score += (10-i)
        else :
            lion_score += (10-i)
    return (lion_score - apeach_score)

def is_better(lion, answer):
    for i in range(10, -1, -1) :
        if answer[i] < lion[i]:
            return True
        elif answer[i] > lion[i]:
            return False

def dfs(apeach, lion, idx, arrow, answer):
    global max_value
    if arrow < 0 :
        return 
    if idx >= 11 :
        # 점수 체크하기
        # 라이언이 완전히 이긴 경우만 answer 를 변경한다

        lion[10] = lion[10] + arrow
        score = calc_score(apeach, lion)
        if score <= 0 :
            return
        if score >= max_value:
            if score == max_value:
                if is_better(lion, answer):
                    answer[:] = lion
            else :
                max_value = score
                answer[:] = lion
        return 
    
    else :
        # 어피치가 쏜 것보다 화살이 많이 있을때
        arrow -= (apeach[idx] + 1)
        lion[idx] = apeach[idx] + 1
        dfs(apeach, deepcopy(lion), idx+1, arrow, answer)
        arrow += (apeach[idx] + 1)
        lion[idx] = 0

        # 점수를 얻지 않는 경우
        dfs(apeach, deepcopy(lion), idx+1, arrow, answer)


max_value = 0
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))