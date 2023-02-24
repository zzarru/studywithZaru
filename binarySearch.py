def binarySearch(a, N, key):
    start = 0
    end = N-1
    cnt = 1
    while start <= end:
        middle = (start + end) // 2

        if a[middle] == key:
            return cnt
        elif a[middle] > key:
            end = middle - 1
            cnt += 1
        else:
            start = middle + 1
            cnt += 1
    return -1

a = [1,2,3,4,5,6,7,8,9,10, 11, 12, 13, 14, 15]
N = 15
key = 3
result = binarySearch(a,N,key)

print(result)