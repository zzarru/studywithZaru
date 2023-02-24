# 리스트에서 번갈아가며 큰수, 작은 수 뽑기
lst = [8, 11, 16, 28, 39, 49, 49, 60, 67, 85, 89, 90]
l = len(lst)

special_lst = []
if len(lst) % 2: # 홀수개의 리스트라면 -> 중복되는 값을 어떻게 한번만 넣을까
    for i in range(l//2+1): # 홀수개의 경우 중앙에도 접근해야하기 때문에 범위를 +1 한다.
        special_lst.append(lst[l-1-i])
        if lst[i] != lst[l-1-i]:  # 조건문 추가 -> 큰값과 작은값이 같지 않을 때만 추가 
            special_lst.append(lst[i])
        
else: # 짝수개의 리스트
    for i in range(l//2): 
        special_lst.append(lst[l-1-i])
        special_lst.append(lst[i])


print(special_lst)