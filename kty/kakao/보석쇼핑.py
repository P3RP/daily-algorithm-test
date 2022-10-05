'''
******* 문제 푼 후 느낀 것 *********
처음에는 dictionary 에 보석들을 모두 넣고, 보석이 모두 1인지 확인했었다.
그 결과 매번 체크함수를 돌리게 되고, 이것이 보석의 종류가 100,000개라면 100,000개를 모두 확인하기 떄문에 오랜 시간이 걸리게된다.
따라서 그렇게 하지않고, 보석을 dict 에 0개라면 지우는 방식으로 구현하니 통과할 수 있었다.
'''

'''
2022/09/22
https://school.programmers.co.kr/learn/courses/30/lessons/67258
보석쇼핑
'''

def solution(gems):
    answer = [0, 0]
    
    gem_dict = dict()
    kind_gem = len(set(gems))
    start = 0
    end = 0
    
    gem_dict[gems[start]] = 1

    all_buy = False
    min_length = 1000000
    
    # 어차피 모든 보석을 구매하려면 gem_dict에 있는 수만큼 남아있어야 한다.
    while(start <= end):
        # 모든 보석을 이전에 다 구매한 경우
        # start 를 키운다.
        all_buy = len(gem_dict) == kind_gem
        print(gem_dict)
        if all_buy :
            if min_length > (end-start+1) :
                min_length = end-start+1
                answer[0] = start+1
                answer[1] = end+1
            if gem_dict[gems[start]] == 1 :
                del(gem_dict[gems[start]])
            else :
                gem_dict[gems[start]] -= 1
            start += 1
        else :
            if end >= len(gems)-1 :
                break
            end += 1
            if gems[end] not in gem_dict:
                gem_dict[gems[end]] = 1
            else : 
                gem_dict[gems[end]] += 1
    
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))