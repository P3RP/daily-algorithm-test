def solution(N, stages):
    answer = []
    
    # 실패율이 높은 스테이지의 번호를 순서대로 담는다.
    stage_user_dict = dict()

    for item in range(N+1):
        stage_user_dict[item+1] = 0
    
    for stage in stages:
        stage_user_dict[stage] += 1
    
    rest = len(stages)
    
    for key in range(N+1):
        if rest == 0 :
            break
        
        fail_user = stage_user_dict[key+1]
        stage_user_dict[key+1] = fail_user/rest
        rest = rest - fail_user
    
    sorted_dict = sorted(stage_user_dict, key=lambda x:stage_user_dict[x], reverse=True)
    
    for key in sorted_dict:
        if key != N+1:
            answer.append(key)
    
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))