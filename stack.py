T = int(input())
for test in range(1, T+1):
    letters = input()

    stack = [0]*10
    top = -1 # 초기 top의 값 설정

    for i in letters:
        if i == '(' or i == '{':
            top += 1
            stack[top] = i

        if i == ')':
            if stack[top] == '(':
                top -= 1
            else:
                top -= 100


        if i == '}':
            if stack[top] == '{':
                top -= 1
            else:
                top -= 100
        print(i, top, stack[i])


    # if top == -1:
    #     print(f'#{test} 1')
    #
    # else:
    #     print(f'#{test} 0')
    