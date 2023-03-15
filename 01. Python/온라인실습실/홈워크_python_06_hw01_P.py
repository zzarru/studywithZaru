# 입력 예시
# # mass percent.py 실행 시
# 1.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 1% 400g
# 2.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 8% 300g
# Done

# 출력 예시
# 4.0% 700.0g


percent = int(input('농도를 입력하세요: '))
salts = int(input('소금의 양을 입력하세요: '))
run = input('done을 입력하면 결과가 출력됩니다.')

if run == 'done':
    print(f'{salts / percent * 100} %')