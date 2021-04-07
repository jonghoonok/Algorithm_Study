# 원형 큐
n = 4
Q = [0]*n
front, rear = 0, 0

def isEmpty():
    return front == rear

def isFull():
    return (rear + 1) % n == front

def enQueue(item):
    global rear
    if (rear+1) % n == front:
        print("Queue Full")
    else:
        rear = (rear + 1) % n
        Q[rear] = item

def deQueue():
    global front
    if front == rear:
        print("Queue Empty")
    else:
        front = (front + 1) % n
        return Q[front]          # front 자리에는 채우지 않음

def Qpeek():
    if front == rear:
        print("Queue Empty")
    else:
         return Q[(front + 1) % n]

enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())
enQueue(4)
print(deQueue())

print(Q)