class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head


    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        node.left = new
        new.left, new.right = node, n
        n.left = new0


    def _del(self, node: ListNode):
        n = node.left.left
        node.left = n
        n.right = node


    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.len == self.k:
            return False
        
        self.len += 1
        self._add(self.head, ListNode(value))
        return True


    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.len == self.k:
            return False
        
        self.len += 1
        self._add(self.tail, ListNode(value))
        return True

        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.len == 0:
            return False
        
        self.len -= 1
        self._del(self.head)
        return True
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.len == 0:
            return False
        
        self.len -= 1
        self._del(self.tail)
        return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.head.value if self.len != 0 else -1
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self.tail.value if self.len != 0 else -1
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.len == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.len == self.k
        