# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # 내부의 값을 변경하는 풀이
    def swapPairs_1(self, head: ListNode) -> ListNode:
        root = head
        while head and head.next:
            head.val, head.next.val = head.next.val, head.val
            head = head.next.next
        return root

    # 문제에서 요구하는 풀이: 내부의 값을 변경하지 않는 풀이
    def swapPairs_2(self, head: ListNode) -> ListNode:6
        root = prev = ListNode(0)
        prev.next = head
        while head and head.next:
            # swap two elements
            node = head.next
            head.next = node.next
            node.next = head

            prev.next = node

            # move to next
            head = head.next
            prev = prev.next.next

        return root