word1 = input('첫 번째 이름을 입력하세요 : ')
word2  = input('두 번째 이름을 입력하세요 : ')

name1 = list(map(str, word1))
name2 = list(map(str, word2))

askii1 = []
for i in name1:
    askii1.append(ord(i))

askii2 = []
for i in name2:
    askii1.append(ord(i))

if sum(askii1) > sum(askii2):
    print(word1)
else:
    print(word2)