Q = []

Q. append(1)
print(Q)
Q. append(2)
print(Q)
Q. append(3)
print(Q)

print(Q.pop(0))
print(Q)
print(Q.pop(0))
print(Q)
print(Q.pop(0))

# pop(0)은 시간이 걸리기 때문에 dequeue를 쓰는 것이 좋음
# 파이썬 내장 자료구조 queue를 쓰면 더 느리기 때문에 비추

# dequeue
import collections
deq = collections.deque()

deq.append(1)
deq.append(2)
deq.append(3)

print(deq.popleft())
print(deq.popleft())
print(deq.popleft())