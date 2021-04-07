# C에서는 front, rear를 이용하여 다음과 같이 작성함
Q = [0]*100
front, rear = -1, -1

def Qpeek():
    if front == rear:
        print("Queue Empty")
    else:
        return Q[front+1]


def enQueue(item):
    global rear
    if rear == len(Q) - 1:
        print("Queue Full")
    else:
        rear += 1
        Q[rear] = item


# 값 자체를 지우는 것이 아니라 front로 덮어씌움
def deQueue():
    global front
    if front == rear:
        print("Queue Empty")
    else:
        front += 1
        return Q[front]

# queue를 전부 다 채운 후에 전부 dequeue하게되면 full이면서 동시에 empty
# 이게 배열의 문제점인데, 값은 차있지만 못 쓰게 됨: 컴퓨터에서 휴지통에 넣은 파일처럼 됨
# 해결하기 위해 deque가 발생할 때 1. 파이썬처럼 원소를 전부 앞으로 이동시키거나
# 2. 원형 queue를 이용하는 방법이 있음: rear = (rear + 1) % n
