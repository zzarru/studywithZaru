s = input('숫자를 입력해주세요 : ')

numbers = list(map(int,str(s))) # 숫자를 잘라서 리스트로 만든다

sum_numbers = sum(numbers) # 리스트의 객체를 더하면 된다..

print(sum_numbers) # 각 자릿수를 더한 값이 출력됨..