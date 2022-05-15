import sys
input = sys.stdin.readline


N = int(input())
zero = []
one = []
pos = []
neg = []

for _ in range(N):
    num = int(input())
    if num == 0:
        zero.append(num)
    elif num == 1:
        one.append(num)
    elif num < 0:
        neg.append(num)
    else:
        pos.append(num)

answer = 0

# 양수 처리
l = len(pos)
pos.sort()
while l > 1:
    answer += pos.pop() * pos.pop()
    l -= 2
if pos:
    answer += pos.pop()

# 음수 처리
l = len(neg)
neg.sort(reverse=True)
while l > 1:
    answer += neg.pop() * neg.pop()
    l -= 2
if neg:
    if not zero:
        answer += neg.pop()

answer += len(one)

print(answer)
