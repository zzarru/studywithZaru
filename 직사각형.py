lst = [[0] * 100 for _ in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    # 해당 좌표 색칠
    for i in range(x1, x2):
        for j in range(y1, y2):
            lst[i][j] = 1

ans = 0
for i in range(100):
    ans += sum(lst[i])

print(ans)