# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        node = head
        cnt = 1
        while cnt < left - 1:
            node = node.next
            cnt += 1
        prev = node
        node = prev.next
        cnt += 1
        while cnt < right - 1:
            