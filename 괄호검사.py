# 괄호검사 => 괄호 {}, ()가 제대로 짝을 이루었는지 검사한다. 
T = int(input())
for test in range(1, T+1):
    letters = input()

    stack = []
    for i in letters:
        # 오른쪽 괄호가 나오면 냅다 stack에 넣어주기
        if i in '({': # i == '(' or i == '{' 를 간단히 이렇게 표현할 수 있다! (근데 i == '(' or '{' 이렇게 생략해서 쓰면 안됨.. )
            stack.append(i)

        elif i == ')':
            # 왼쪽 괄호 나오면 stack이 비어있지 않고 stack의 top에 있는 괄호와 짝이 맞을 경우 stack에 있는 요소를 pop(제거)해준다.
            if stack and stack[-1] == '(':
                stack.pop()

            # stack이 비어있는데 왼쪽 괄호가 나오거나 stack이 비어있지 않지만 top과 짝이 맞지 않을 경우, stack에 오른쪽 괄호 넣어주고 break해준다. (굳이 letters 전체를 돌지 않아도 오류이기 때문에)
            else:
                stack.append(i)
                break

        elif i == '}':
            if stack and stack[-1] == '{':
                stack.pop()

            else:
                stack.append(i)
                break

    if stack: # 스택에 뭔가 남아있으면 짝이 맞지 않은 경우이므로 0 출력
        print(f'#{test} 0')

    else: # 스택이 비어있으면 짝이 맞으므로 1 출력 ㅊㅋㅊㅋ
        print(f'#{test} 1')    