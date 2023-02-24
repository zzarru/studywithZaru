# 인접행렬 matrix 만들기
# visited 각 노드 방문 여부 리스트
# 노드가 1부터 시작하는 경우, matrix와 visited의 크기를 +1한다. (인덱스 0을 포함하기 때문에)
# N = 노드 개수
# M = 간선 개수

matrix = [[0]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(M):
    f, t = map(int, input().split()) # f는 행, t는 열
    matrix[f][t] = matrix[t][f] = 1

    def dfs(matrix, s, visited):
        stack = [s] # 시작 정점을 우선 stack에 넣고 시작한다.
        while stack: # stack이 있을 때까지 반복한다. 
            value = stack.pop() # stack에서 pop한 요소 -> 방문여부 확인하기
            if not visited[value]: # visited에 value가 false면 방문한 적 없으므로,
                visited[value] = True # 방문여부를 True로 바꿔준다.
            
            for i in range(len(matrix[value])): # matrix의 value행을 순회하며 child 노드탐색
                if matrix[value][i] == 1 and not visited[i]: # child 노드이면서 방문한 적 없다면
                    stack.append(i) # stack에 추가한다 -> 계속 반복
