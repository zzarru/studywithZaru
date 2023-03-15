# fn_d(91) 
# 출력 예시 
# 101

def fn_d(n):
    n_str = str(n)
    numbers = list(map(int, n_str))

    return n + sum(numbers)

n = 91
print(fn_d(n))
