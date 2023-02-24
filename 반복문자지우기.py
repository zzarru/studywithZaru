T = int(input())
for test in range(1, T+1):
    s = input()

    stack = []
    for i in s: # 문자열 순회하면서 
        if stack: # 스택이 비어있지 않다면
            if i == stack[-1]: # i와 top이 같은 경우 stack에서 pop
                stack.pop()
            else: # i와 top이 다른 경우 stack에 저장
                stack.append(i)

        else: # 스택이 비어있는 경우에는 냅다 넣어줘~
            stack.append(i)

    print(f'#{test} {len(stack)}')