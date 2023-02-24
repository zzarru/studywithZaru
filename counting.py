num_list = [0, 4, 1, 3, 1, 2, 4, 1]
sort_list = [0] * (len(num_list)) # temp 만들기..
max = max(num_list) # 정렬 안의 최고값 찾기

counts = [0] * (max + 1) # max+1개의 카운트 배열 만들기

for i in range(len(num_list)): # 아무것도 넣지 않을 때 _(언더바) 사용
    print(counts[num_list[i]]) += 1

for i in range(1, len(counts)): # 이미 생성된 counts 배열에서 누적합을 구한 배열을 만든다. 첫번째 값은 그대로 내린다. 
    # print(couts[i]) # 3
    # print(counts[i-1]) # 1 # 그 전 값에 접근하는 방법 == 인덱싱을 이용한다. 
    counts[i] += counts[i-1] # 누적값을 구한다. # [ 1 4 5 6 8]

# 다시 data를 끝에서 부터 돌면서 counts에 있는 값을 확인하고 temp에 저장한다. 리스트의 개수만큼 반복한다. 
# for i in range(len(num_list), 0, -1): # num_list의 길이는 8이라서 8부터 시작, 0부터 시작, -1 인덱스부터 돈다.
    #벗.. i라는 변수를 사용하지 못할 것 (인덱스에러) -> why? 시작하는 값이 8인데 num_list에는 인덱스  8이 없음
    # 따라서 -1을 해줘야한다. 

for i in range(len(num_list), -1, -1, -1): # 0의 값도 가져와야하므로 0을 -1로 바꿔준다. 
    sort_list[counts[num_list[i]]] = num_list[i]
    counts[num_list[i]] -= 1

print(sort_list)