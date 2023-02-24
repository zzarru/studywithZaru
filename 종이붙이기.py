# 종이 붙이기 함수 만들기
def paper(N):
    if N == 1:
        return 1
    
    elif N == 2:
        return 3
    
    else:
        return paper(N-1) + paper(N-2)*2


T = int(input())
for test in range(1, T+1):
    N = int(input())
    N = N//10

    print(f'#{test} {paper(N)}')