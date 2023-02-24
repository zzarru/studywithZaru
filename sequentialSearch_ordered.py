# 순차 검색 (정렬되어 있는 경우 ; 오름차순 기준)
def sequentialSearch2 (A, key, N):
    i = 0
    while i < N and A[i] < key:
        i += 1

    if i < N and A[i] == key:
        return i

    else:
        return -1


A = [1, 3, 5, 8, 10, 13, 15]
N = len(A)
key = 10

result = sequentialSearch2(A, key, N)

print(result)  