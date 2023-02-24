a = 'level'
b = 'level     '

print(len(b)) # 문자열도 len함수 쓸 수 있구낭..

cnt = 0
for i in b: # 그것도 모르고 또 하드코딩의 삶.. 그나저나 공백 포함 길이를 재주는 군
    cnt += 1

print(cnt)