def count(lst):
    mx = 2
    for i in lst:
        cnt = 0
        for j in i:
            if j:
                cnt += 1
                if mx < cnt:
                    mx = cnt
            else:
                cnt = 0

    return mx

T = int(input())
for test in range(1, T + 1):
    N, M = map(int, input().split())
    data_lst = [list(map(int, input().split())) for _ in range(N)]
    data_lst_t = list(map(list, zip(*data_lst)))

    mx_horizon = count(data_lst)
    mx_vertical = count(data_lst_t)

    if mx_horizon > mx_vertical:
        print(f'#{test} {mx_horizon}')
    else:
        print(f'#{test} {mx_vertical}')