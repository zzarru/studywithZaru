# for문 이용하여 문자열 뒤집기
letters = list(map(str, input()))
length = len(letters)

# 바꾸기 기준점 
middle = length // 2 - 1

for i in range(middle+1):
    letters[i], letters[length-1-i] = letters[length-1-i], letters[i]


for i in range(length):
    print(letters[i], end='')
