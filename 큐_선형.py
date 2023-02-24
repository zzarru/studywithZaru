# Queue 구현하기
queue = [0]*10
front = -1
rear = -1

def enQueue(item):
    global rear
    if front != rear and rear == len(queue) - 1: # 비어있지 않고 rear가 리스트의 마지막 값을 가리키고 있지 않을 때
        print("isFull!")
    
    else:
        rear += 1
        queue[rear] = item
    
def deQueue():
    global front
    if front == rear:
        print("isEmpty!")
    
    else:
        front += 1  
    
    return queue[front]


enQueue(1)
enQueue(2)
enQueue(3)

print(deQueue())
print(deQueue())
print(deQueue())

if front != rear:
    print(deQueue())