N = 3
lst = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    max = 0
    for j in range(N):
        if lst[j][i] > max:
            max = lst[j][i]

    if i % 2 == 0:
        print(i, max)