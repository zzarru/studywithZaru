def perm(i, k):
    if i == k:
        print(*p)
    else:
        for j in range(k): # 사용하지 않은 숫자를 used에서 찾는다.
            if used[j] == 0:
                p[i] = A[j]
                used[j] = 1 # j번 자리 숫자 사용으로 표시한다. 
                perm(i+1, k)
                used[j] = 0 # j번 자리 숫자 다른 자리에서 쓸 수 있게 원상복구


A = [1,2,3]
p = [0]*3
used = [0]*3
perm(0,3)

'''
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1

--> 사전순으로 정렬된다. 
'''