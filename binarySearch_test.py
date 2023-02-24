page = 400
mark = 50
start = 1
end = page
cnt = 1

while start < end:
    middle = (start + end) // 2
    if middle == mark:
        print(cnt)
        break

    elif middle < mark:
        start = middle + 1
        cnt += 1

    else:
        end = middle -1
        cnt += 1

