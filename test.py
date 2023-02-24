num = 456789
c = [0] * 12

for i in range(6) :
    c[num % 10] += 1
    num //= 10


print(c)