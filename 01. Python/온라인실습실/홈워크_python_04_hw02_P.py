words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

slice = []
for i in words:
    slice.append(list(map(str, i)))
    for j in slice:
        j.sort()

dic_words = {i : slice[i] for i in range(len(slice))}

print(dic_words)


    