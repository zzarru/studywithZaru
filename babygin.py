num = 456789
c = [0] * 12 # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트

#print(num / 10)

for i in range(6) :
    #print(num % 10)  # 9
    c[num % 10] += 1 # c[9] += 1
    num //= 10
#   num = num / 10


print(c)

i = tri = run = 0
while i < 10 : #i = 0 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6 -> 7 -> 7 -> 8 -> 9 -> 10
    if c[i] >= 3 : # triplete 조사 후 데이터 삭제
        c[i] -= 3
        tri += 1
        continue;
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1 : # run 조사 후 데이터 삭제
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1 # 1 2
        continue;
    i += 1

if run + tri == 2 :
    print("Baby Gin")
else :
    print("Lose")