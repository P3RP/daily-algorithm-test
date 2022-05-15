num_number = int(input())

num_list_pos = []
num_list_zero = 0
num_list_neg = []

for index in range(num_number):
    num = int(input())
    if(num > 0):
        num_list_pos.append(num)
    elif(num < 0):
        num_list_neg.append(num)
    else:
        num_list_zero += 1

num_list_pos.sort() 
num_list_neg.sort()
num_list_neg.reverse()

sum = 0

while (len(num_list_pos) >= 2):
    first_pop = num_list_pos.pop() 
    second_pop = num_list_pos.pop()
    if(first_pop == 1 and second_pop == 1):
        sum += 2
        continue
    elif(second_pop == 1):
        sum += (1 + first_pop)
        continue
    else:
        sum += first_pop * second_pop

for index in range(len(num_list_pos)):
    sum += num_list_pos[index]

while (len(num_list_neg) >= 2):
    if((len(num_list_neg) % 2 == 1) and num_list_zero > 0):
        del num_list_neg[0]
        num_list_zero -= 1
    sum += num_list_neg.pop() * num_list_neg.pop()

for index in range(len(num_list_neg)):
    if not(num_list_zero):
        sum += num_list_neg[index]

print(sum)