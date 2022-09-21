from copy import deepcopy


answer = 0
checked_list = []
def solution(user_id, banned_id):
    dfs(user_id, banned_id, 0, [0 for _ in range(len(user_id))])
    return answer

def dfs(user_id, banned_id, banned_id_idx, checked):
    global answer

    if banned_id_idx == len(banned_id):
        exist = False
        for i in checked_list:
            if i == checked:
                exist = True
                break
            
        if not exist:
            answer += 1
            checked_list.append(checked)
    
        return
    
    else:
        for i in range(len(user_id)):
            if checked[i] == 1:
                continue
            else:
                if (check(user_id[i], banned_id[banned_id_idx])):
                    checked[i] = 1
                    dfs(user_id, banned_id, banned_id_idx+1, deepcopy(checked))
                    checked[i] = 0

def check(target, compare):
    if len(target) != len(compare):
        return False
    
    for i in range(len(compare)):
        if compare[i] == '*':
            continue
        
        if compare[i] != target[i]:
            return False
    return True

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))