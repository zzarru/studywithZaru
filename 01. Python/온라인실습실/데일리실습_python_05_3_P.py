# 입력 예시
# s = '@#~I NeVEr DrEamEd AbouT SuCCeSs, i woRkEd foR iT.!>!'

# 출력 예시
# 'I never dreamed about success, i worked for it.'

s = input()
low_s = s.lower()[3:-3]

cap_s = low_s.capitalize()
print(cap_s)
