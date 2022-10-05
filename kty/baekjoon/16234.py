'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/10/05
boj.kr/16234
인구 이동
'''
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())




country_list = []


for _ in range(N):
    country_list.append(list(map(int, input().split())))

count = 0
move = [(0,1), (1,0)]
while(count<2001):
    is_move = False
    # 결합되었는지 확인하는 용도
    union_list = [[0 for _ in range(N)] for _ in range(N)]
    union_dict = dict()
    country_num = 0

    # 모든 칸을 한번씩 방문해나간다.
    for x in range(N):
        for y in range(N):
            for i, j in move:
                next_x = i + x
                next_y = j + y        
                if 0 <= next_x < N and 0 <= next_y < N and L <= abs(country_list[x][y] - country_list[next_x][next_y]) <= R:
                    is_move = True
                    # 방문 처리를 한다.
                    # 이때 이전에 있던 구역이 연합을 맺지 않았다면
                    # 마을 번호를 하나 올려준다.
                    if union_list[x][y] == 0 and union_list[next_x][next_y] == 0:
                        country_num += 1
                        union_list[x][y] = country_num
                        union_list[next_x][next_y] = country_num
                        union_dict[country_num] = (2, country_list[x][y] + country_list[next_x][next_y])
                    
                    # 이미 연합을 맺은 곳이라면 추가만 해준다
                    elif union_list[x][y] != 0 and union_list[next_x][next_y] == 0:
                        union_list[next_x][next_y] = union_list[x][y]
                        a, b = union_dict[union_list[x][y]]
                        union_dict[union_list[x][y]] = (a+1, b+country_list[next_x][next_y])
                    
                    elif union_list[next_x][next_y] != 0 and union_list[x][y] == 0:
                        union_list[x][y] = union_list[next_x][next_y]
                        a, b = union_dict[union_list[x][y]]
                        union_dict[union_list[x][y]] = (a+1, b+country_list[x][y])
                    
                    elif union_list[next_x][next_y] != 0 and union_list[x][y] != 0 and union_list[next_x][next_y] != union_list[x][y]:
                        before_a, before_b = union_dict[union_list[x][y]]
                        del union_dict[union_list[x][y]]
                        change_v = union_list[x][y]
                        for k in range(N):
                            for l in range(N):
                                if union_list[k][l] == change_v:
                                    union_list[k][l] = union_list[next_x][next_y]
                        a, b = union_dict[union_list[next_x][next_y]]
                        union_dict[union_list[next_x][next_y]] = (a+before_a, b+before_b)
    # 값 업데이트   
    for key in union_dict:
        a, b = union_dict[key]
        new_v = b // a
        for i in range(N):
            for j in range(N):
                if union_list[i][j] == key:
                    country_list[i][j] = new_v

    # 움직였다면 반복문을 계속 수행한다.
    if is_move:
        count += 1
        continue
    # 그렇지 않다면 멈춘다.
    break

print(count)