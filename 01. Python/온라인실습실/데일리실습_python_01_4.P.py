n = int(input())

numbers = list(range(1,n)) 

double = [] # 2의 배수 리스트
for i in numbers:
    if i % 2 == 0:
        double.append(i)
    
seven_times = [] # 7의 배수 리스트
for j in numbers:
    if j % 7 == 0:
        seven_times.append(j)


total = sum(double)+sum(seven_times) # 2, 7배수의 총합

print(total)