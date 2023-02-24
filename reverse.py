s = 'Reverse this strings'

s = list(s) #  문자열 리스트화하기
s.reverse() # 리스트 뒤집기
s = ''.join(s) # 작은따옴표('') 사이 비워두면 공백 없이 문자열 합치기
print(s)