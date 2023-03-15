students = ['박해피', '이영희', '조민지', '조민지', 
            '김철수', '이영희', '이영희', '김해킹',
            '박해피', '김철수', '한케이', '강디티',
            '조민지', '박해피', '김철수', '이영희',
            '박해피', '김해킹', '박해피', '한케이','강디티']

key = [] # 혈액형 종류
for i in students:
    if i not in key:
        key.append(i)

vote = [] # 획득수
for i in key:
    cnt = 0
    for j in students:
        if i == j:
            cnt += 1
    vote.append(cnt)

dic_vote = dict(zip(key, vote))
print(dic_vote)
