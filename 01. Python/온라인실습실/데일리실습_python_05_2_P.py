import calc

def add(n,m):
    return n+m

def sub(n,m):  
    return n-m

def mul(n,m):
    return n*m

def div(n,m):
    if m ==0:
        return('0으로 나눌 수 없습니다.')
    else:
        return n / m



print(calc.add(2, 3)) # 5
print(calc.sub(2, 3)) # -1
print(calc.mul(2, 3)) # 6
print(calc.div(2, 3)) # 0.6666666666666666

print(calc.div(2, 0)) # 0으로 나눌 수 없습니다.