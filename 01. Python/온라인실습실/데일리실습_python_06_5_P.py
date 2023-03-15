# sum_of_digit(3904) # 16

def sum_of_digit(num):
    num_str = str(num)
    num_list = [int(num_str[0]), int(num_str[1]), int(num_str[2]), int(num_str[3])]
    return sum(num_list)

print(sum_of_digit(3904))
