def perm(i, k): # i 값을 결정할 자리, k 결정할 개수
    if i == k:
        print(*p)
    else:
        for j in range(i, k): # 자신부터 오른쪽 원소들과 자리 교환
            p[i], p[j] = p[j], p[i]
            perm(i+1, k)
            p[i], p[j] = p[j], p[i]


p = [1,2,3]
perm(0,3)