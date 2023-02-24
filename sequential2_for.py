# 순차 검색 (정렬되어 있는 경우; for문)
def sequentialSearch2 (A, key, N):
    for i in range(N):
        if A[i] == key:
            return i
        elif A[i] > key:
            return -1


A = [1, 3, 5, 8, 10, 13, 15]
N = len(A)
key = 5

result = sequentialSearch2(A, key, N)

print(result)  



        # if A[i] <= key:
        #     if A[i] < key:
        #         pass
        #     if A[i] == key:
        #         return i

        # else:
        #     return -1