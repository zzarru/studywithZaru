T = int(input())
for test in range(1, T + 1):
    N, M = map(int, input().split())
    data_lst = [list(map(int, input().split())) for _ in range(N)]
    data_lst_t = list(map(list, zip(*data_lst)))

    # 행 우선 탐색
    max_cnt = 2
    for i in data_lst:
        cnt = 0
        for j in i:
            if j:
                cnt += 1
                if cnt > max_cnt:
                    max_cnt = cnt
            else:
                cnt = 0

    for i in data_lst_t:
        cnt = 0
        for j in i:
            if j:
                cnt += 1
                if cnt > max_cnt:
                    max_cnt = cnt
            else:
                cnt = 0
 
    print(f'#{test} {max_cnt}')