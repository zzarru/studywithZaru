T = int(input())
for test in range(1, T + 1):
    N, M = map(int, input().split())
    data_lst = [list(map(int, input().split())) for _ in range(N)]
 
    # 행 우선 탐색
    max_cnt = 2
    for i in range(N):
        cnt = 0
        for j in range(M):
            if data_lst[i][j]:
                cnt += 1
                if cnt > max_cnt:
                    max_cnt = cnt
            else:
                cnt = 0
 
 
    # 열 우선 탐색
    for i in range(N):
        cnt = 0
        for j in range(M):
            if data_lst[j][i]:
                cnt += 1
                if cnt > max_cnt:
                    max_cnt = cnt
 
            else:
                cnt = 0
 
    print(f'#{test} {max_cnt}')