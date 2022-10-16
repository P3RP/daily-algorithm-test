'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/10/16
boj.kr/1446
지름길
'''
import sys
input = sys.stdin.readline

N, D = map(int, input().split())

drive_distance = [i for i in range(D+1)]

shortcut_list = []
for _ in range(N):
    shortcut_list.append(list(map(int, input().split())))

for i in range(0, D+1):
    # 지름길은 start 지점에서 end 지점에 대한 값을 업데이트 해준다.
    # 그렇게되면 추후 확인할때 지름길로 갔을때와 그냥 갔을때를 비교하게 된다.
    if i > 0:
        drive_distance[i] = min(drive_distance[i-1] + 1 , drive_distance[i])

    for start, end, dist in shortcut_list:
        if i == start and end < D+1 and dist + drive_distance[start] < drive_distance[end]:
            drive_distance[end] = dist + drive_distance[start]
    
print(drive_distance[D])