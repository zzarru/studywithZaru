def BFS(G,v):
    visited = [0]*(n+1)
    queue = []
    queue.append(v)

    while queue :
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = True
            # visit(t) 구현할 코드 작성
            
            for i in G[t]:
                if not visited[i]:
                    queue.append(i)
