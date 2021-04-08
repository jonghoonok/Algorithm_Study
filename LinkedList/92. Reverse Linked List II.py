# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or m == n:
            return head
        
        root = node = ListNode(None)
        node.next = head
        for _ in range(left - 1):
            node = node.next
        
        # 뒤집었을 때 가장 마지막이 되는 노드
        end = node.next

        for _ in range(right - left):
            temp, node.next, end.next = node.next, end.next, end.next.next
            node.next.next = temp        
        
        return head