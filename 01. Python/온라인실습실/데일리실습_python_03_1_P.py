bongdari = ['apple', 'rottenBanana','apple','RoTTenorange', 'orange']

little = [] 

# 전부 소문자로 바꾸기
for i in bongdari: 
    little.append(i.lower())

# # rotten 제거하기
for j in little:
    if j[0:6] == 'rotten':
        j = j[7, -1]

print(little)



