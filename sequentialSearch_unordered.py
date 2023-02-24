# 순차 검색 (정렬되어 있지 않은 경우)
def sequentialSerch(A, key, N):
    i = 0
    while i < N and A[i] != key:
        i += 1

    if i < N and A[i] == key: # 키를 찾은 경우 i를 반환
        return i

    else: # key를 찾지 못한 경우 -1을 반환
        return -1


A = [3, 5, 1]
N = len(A)
key = 7

result = sequentialSerch(A, key, N)
print(result)