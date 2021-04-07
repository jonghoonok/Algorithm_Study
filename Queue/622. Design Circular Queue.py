class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None]*k
        self.maxlen = k
        self.f = 0
        self.r = 0

    def enQueue(self, value: int) -> bool:
        if self.q[self.r] is None:
            self.q[self.r] = value
            self.r = (self.r+1)%self.maxlen
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.q[self.f] is not None:
            self.q[self.f] = None
            self.f = (self.f+1)%self.maxlen
            return True
        else:
            return False

    def Front(self) -> int:
        if self.q[self.f] is not None:
            return self.q[self.f]
        else:
            return -1

    def Rear(self) -> int:
        if self.q[self.r-1] is not None:
            return self.q[self.r-1]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        if self.f == self.r and self.q[self.f] is None:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.f == self.r and self.q[self.f] is not None:
            return True
        else:
            return False