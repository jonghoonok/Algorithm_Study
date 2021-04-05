# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            add = 0
            if l1:
                add += l1.val
                l1 = l1.next
            if l2:
                add += l2.val
                l2 = l2.next
            
            carry, val = divmod(add + carry, 10)
            head.next = ListNode(val)
            head = head.next
        
        return root.next