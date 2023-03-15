# num_list = [4, 4, 7, 8, 10, 4]
# sum_of_repeat_number(num_list)

# 출력 예시 
#  25


num_list = [4, 4, 7, 8, 10, 4]
max = max(num_list)
cnt_list = [0] * (max+1)
only_list = []
# def sum_of_repeat_number(num_list)
for i in num_list:
    cnt_list[i] += 1

for i in range(len(cnt_list)):
    if cnt_list[i] == 1:
        only_list.append(i)

print(sum(only_list))