'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/07/21
boj.kr/1806
부분합

문제 :
10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 
이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

입력 :
첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)가 주어진다. 
둘째 줄에는 수열이 주어진다. 수열의 각 원소는 공백으로 구분되어져 있으며, 10,000이하의 자연수이다.

결과 :
첫째 줄에 구하고자 하는 최소의 길이를 출력한다. 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력하면 된다.
'''
import sys
input = sys.stdin.readline

num_count, want_sum = map(int, input().split())

num_list = list(map(int, input().split()))

start = 0
end = 0

min_length = 100001
temp_sum = num_list[0]
while(start <= end and end < num_count) :
    if(temp_sum < want_sum):
        end += 1
        if(end < num_count):
            temp_sum += num_list[end]
    elif(temp_sum >= want_sum) :
        min_length = min(min_length, end-start+1)
        if (min_length == 1):
            break
        start +=1
        temp_sum -= num_list[start-1]
        
if(min_length != 100001):
    print(min_length)
else :
    print(0)