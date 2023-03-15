# 입력 예시
# [1, 1, 3, 3, 0, 1, 1]

# 출력 예시
# [1, 3, 0, 1]

a = list(map(int, input()))
new_a = []
for i in range(len(a)-1):
    if a[i] - a[i+1] !=0:
        new_a.append(a[i])


if a[len(a)-1] - a[len(a)-2] == 0:
    new_a.append(a[len(a)-1])

print(new_a)