'''
******* 문제 푼 후 느낀 것 *********
문제 해설을 보니 dfs로 모든 경우를 확인하는 것이 올바른 해결은 아닌 것 같다.

반복문으로 아이템들을 확인하면서 빈자리가 없는 경우 처리가 가장 중요하다
1. 멀티탭에 있는 제품 중 나중에 사용되지 않는 것을 뺀다.
2. 위의 경우에 해당하지 않는다면, 가장 나중에 사용하는 제품을 고른다

-> 운영체제 메모리 페이지 관리에서 Optimal Page Replacement 방식과 유사한 것 같다.
'''

'''
2022/07/19
boj.kr/1700
멀티탭 스케줄링

문제 :
기숙사에서 살고 있는 준규는 한 개의 멀티탭을 이용하고 있다. 준규는 키보드, 헤어드라이기, 핸드폰 충전기, 디지털 카메라 충전기 등 
여러 개의 전기용품을 사용하면서 어쩔 수 없이 각종 전기용품의 플러그를 뺐다 꽂았다 하는 불편함을 겪고 있다. 그래서 준규는 자신의 생활 패턴을 분석하여, 자기가 사용하고 있는 전기용품의 사용순서를 알아내었고, 이를 기반으로 플러그를 빼는 횟수를 최소화하는 방법을 고안하여 보다 쾌적한 생활환경을 만들려고 한다.

예를 들어 3 구(구멍이 세 개 달린) 멀티탭을 쓸 때, 전기용품의 사용 순서가 아래와 같이 주어진다면, 

키보드
헤어드라이기
핸드폰 충전기
디지털 카메라 충전기
키보드
헤어드라이기
키보드, 헤어드라이기, 핸드폰 충전기의 플러그를 순서대로 멀티탭에 꽂은 다음 디지털 카메라 충전기 플러그를 꽂기 전에 핸드폰충전기 플러그를 빼는 것이 최적일 것이므로 플러그는 한 번만 빼면 된다. 

입력 :
첫 줄에는 멀티탭 구멍의 개수 N (1 ≤ N ≤ 100)과 전기 용품의 총 사용횟수 K (1 ≤ K ≤ 100)가 정수로 주어진다. 
두 번째 줄에는 전기용품의 이름이 K 이하의 자연수로 사용 순서대로 주어진다. 각 줄의 모든 정수 사이는 공백문자로 구분되어 있다. 

결과 :
하나씩 플러그를 빼는 최소의 횟수를 출력하시오. 
'''
import sys
input = sys.stdin.readline

hole_count, item_count = map(int, input().split())

hole = [-1] + [0 for _ in range(hole_count)]
item_list = list(map(int, input().split()))

min_count = 999999999
def dfs(count=0, recursion=0):
    global hole
    global item_list
    global min_count

    if count >= min_count:
        return

    if(recursion >= item_count):
        min_count = min(min_count, count)
        return
    
    else :
        i = item_list[recursion]
        # 이미 구멍에 있다면 그냥 개수만 빼주기
        if i in hole :
            dfs(count = count, recursion = recursion + 1)
        # 비어있는 구멍이 있다면 그곳에 넣기
        elif(0 in hole):
            empty_hole = hole.index(0)
            hole[empty_hole] = i
            dfs(count=count , recursion = recursion + 1)
            hole[empty_hole] = 0
        
        # 없다면 구멍 하나에서 빼야한다
        else:
            for j in range(1, len(hole)):
                before_hole_item = hole[j]
                hole[j] = i
                count += 1
                dfs(count = count, recursion = recursion + 1)
                hole[j] = before_hole_item
                count -= 1


dfs(0, 0)
print(min_count)



