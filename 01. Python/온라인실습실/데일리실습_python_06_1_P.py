# A. 입력예시
# print(de_identify('970103-1234567'))
# print(de_identify('8611232345678'))

# B. 출력예시
# 970103*******
# 861123******* 

def de_identify(id):
    id_str = str(id)
    if len(id_str) == 14:
        id_pw = id_str[:7] + '******'

    elif len(id_str) == 13:
        id_pw = id_str[:6] + '******'

    return id_pw

print(de_identify('970103-1234567'))
print(de_identify('8611232345678'))