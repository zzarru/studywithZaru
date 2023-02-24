def cut(n):
    cut = [0]*(n+1)
    cut[0] = 1
    cut[1] = 3
    for i in range(2, n+1):
        cut[i] = cut[i-1] + (cut[i-2] * 2)

    return cut[n]

print(cut(2))