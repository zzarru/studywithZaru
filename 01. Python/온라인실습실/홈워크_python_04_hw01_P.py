words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

fails = []
for i in range(len(words)-1):
    if words[i][-1] != words[i+1][0]:
        fails.append(words[i+1])

dup = []
for i in range(len(words)-1):
    if words[i+1] in words[:i+1]:
        dup.append(words[i+1])

fail_lst = []
for i in fails:
    fail_lst.append(words.index(i)+1)

for j in dup:
    fail_lst.append(words.index(j)+2)

print(f'탈락자 번호는 {fail_lst}번 입니다.')