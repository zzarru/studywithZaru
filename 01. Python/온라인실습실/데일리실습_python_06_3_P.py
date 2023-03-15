# count_vowels('apple') #=> 2
# count_vowels('banana') #=> 3

def count_vowels(letters):
    vowels = 'aeiou'
    cnt = 0
    for i in letters:
        if i in vowels:
            cnt += 1
    return cnt

print(count_vowels('banana'))
