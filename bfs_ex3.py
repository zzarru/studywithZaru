'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

'''
def BFS(graph, start):
    visited = [0]*(N+1)
    queue = []
    queue.append(start)
    visited[start] = 1

    path = []
    while queue :
        t = queue.pop(0)
        path.append(t)

        for i in graph[t]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[N] + 1

    return path


# 그래프(인접리스트)로 구현하기
N, E = map(int, input().split()) # N = 노드의 개수, E = 간선의 개수
lst = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for i in range(E):
    f, t = lst[i*2], lst[i*2+1]
    graph[f].append(t)
    graph[t].append(f) # 양방향 그래프

print(BFS(graph, 4))