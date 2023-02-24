def bfs(si, sj, ei, ej):
    # [0] q, visited 및 필요 변수 생성
    q = []
    v = [[0] *N for _ in range(N)]

    # 1) q에 초기데이터 삽입, v표시 및 필요한 작업
    q.append((i, sj, 0))
    v[si][sj] = 1

    while q:
        # 2) q에서 데이터 한개 꺼냄 (필요시 정답처리)
        ci, cj, d = q.pop(0)
        if ci == ei and cj == ej:
            return d-1

            # 3) 4/8방향, 연결 + 조건에 맞으면 큐 삽입
            for di, dj in ([-1,0], [1,0], [0,-1], [0,1]):
                ni, nj = ci, + di, cj + dj
                if 0 <= ni < N and 0 <= nj < N and \
                    v[ni][nj] == 0 and arr[ni][nj] != '1':
                    q.append((ni, nj, d+1))
                    v[ni][nj] = 1
    
    # 목적지 등 찾을 수 없는 경우 리턴 값
    return 0 