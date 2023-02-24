# 원형 큐 구현하기
queue = [0]*4
front = rear = 0

def enQueue(item):
    global rear
    rear = (rear + 1) % len(queue)
    queue[rear] = item

def deQueue():
    global front
    front = (front + 1) % len(queue)

    return queue[front]


enQueue(1)
enQueue(2)
enQueue(3)
print(deQueue())
print(deQueue())
print(deQueue())