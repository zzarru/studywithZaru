# 버블 정렬
'''
55 7 78 12 42
for i :  N-1 -> 1 #각 구간의 끝
    for j : - -> i-1 # 비교할 왼쪽 원소
        if arr[j] > arr[j+1]:
            arr[j] <-> arr[j+1] # 큰 원소 오른쪽으로    
'''
a = [55, 7, 78, 12, 42]
N = len(a)

def bubblesort(a, N): # 정렬할 list, Nㅇ 원소의 수 
    for i in range(N-1, 0, -1): # 각 구간의 끝
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

bubblesort(a, N)
print(a)