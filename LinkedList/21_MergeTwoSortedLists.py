# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # l1을 가리킬 것이기 때문에 l2가 더 작다면 바꿔준다
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        # l1의 다음 노드들에 대해 재귀적으로 병합하여 작은 노드들만 계속 가리킨다
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1