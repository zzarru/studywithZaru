# 값이 한 줄로 들어올 때 (양방향 그래프)
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

N, M = map(int, input().split())
arr = list(map(int, input().split()))
matrix = [[0*(N+1) for _ in range(N+1)]]
for i in range(M):
    f, t = arr[i*2], arr[i*2+1]
    matrix[f][t] = 1
    matrix[t][f] = 1

print(matrix)