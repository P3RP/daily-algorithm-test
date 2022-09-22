'''
******* 문제 푼 후 느낀 것 *********
당황스럽다. dfs, bfs로 풀면 절대 불가능하다는 것은 알 수 있었지만 어떻게 풀어야하는지 감이 오지 않았었다.
배열의 크기가 매우 크다면 슬라이딩 윈도우나 이분탐색을 설택해야 할 것 같다.

이때 여기서는 돌맹이의 원소 최대값이 2억으로 이분탐색을 하게되면 이를 활용하여 최대 건널 수 있는 사람을 빠르게 찾을 수 있다.
꼭 기억할 수 있도록 하자.
'''

'''
2022/09/22
https://school.programmers.co.kr/learn/courses/30/lessons/67258
징검다리건너기
'''

def solution(stones, k):
    answer = 0
    
    min_people = 1
    max_people = max(stones)
    
    while(min_people <= max_people):
        mid_people = (min_people + max_people) // 2
        
        # stone 을 건널 수 있다면 더 많은 사람이 건너갈 수 있다는 것
        break_stone = 0
        for stone in stones:
            # stone 이 0 보다 작으면 건너는 것이 불가능해졌다는 것
            # 0 인 경우엔 건너는 것은 가능하다.
            if stone - mid_people < 0 :
                break_stone += 1
            else :
                break_stone = 0
            
            if break_stone == k :
                break
        
        if break_stone >= k :
            max_people = mid_people - 1
        else :
            min_people = mid_people + 1
            answer = max(mid_people, answer)
            
    
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))