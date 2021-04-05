# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # repetition
    def reverseList(self, head: ListNode) -> ListNode:
        rev, node = None, head
        while node.next:
            rev, rev.next, node = node, rev, node.next
        return rev

    # recursive
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
            
        return reverse(head)