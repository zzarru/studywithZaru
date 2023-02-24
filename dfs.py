def dfs(s, g):
    stack = [s]

    while stack:
        value = stack.pop()

        if not visited[value]:
            visited[value] = True

        for i in range(1, value+1):
            if matrix[value][i] == 1 and not visited[i]:
                if i == g:
                    return 1
                stack.append(i)

    return 0

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())

    # 간선정보 나타내는 그래프 만들기 (인접행렬; 이차원배열; 단방향 그래프)
    matrix = [[0]*(N+1) for _ in range(N+1)] # 노드가 1부터 시작하므로 N+1만큼 생성한다. (0 포함)
    for _ in range(M):
        f, t = map(int, input().split())
        matrix[f][t] = 1

    # 방문여부 리스트
    visited = [False]*(N+1)

    # 노드 시작점과 도착점
    s, g = map(int, input().split())

    print(s, g)
    print(dfs(s, g))




