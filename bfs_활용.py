def BFS(G,v):
    visited = [0]*(n+1)
    queue = []
    queue.append(v)
    visited[v] = 1

    while queue :
        t = queue.pop(0)
        # visit(t) 구현할 무언가

        for i in G[t]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[n] + 1