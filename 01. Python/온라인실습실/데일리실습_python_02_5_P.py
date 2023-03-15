todo = [("Python Homework", 3), ("Assay", 4), ("Vacation", 100)]

# 입력 예시
# Soccer Contest
# 10

todo_list = input('해야 할 일을 입력하세요 : ')
d_day = int(input('남은 일수를 입력하세요 : '))
new_todo = (todo_list, d_day)

todo.append(new_todo)

print(todo)
