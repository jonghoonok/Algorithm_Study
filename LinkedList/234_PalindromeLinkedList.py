# 파이썬식 편법: 배열로 만들어버리기
def isPalindrome_1(head) -> bool:
    q = []
    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    n = len(q)
    for i in range(n//2):
        if q[i] != q[n-i-1]:
            return False
    return True


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 원래 문제가 의도한 풀이: Runner를 이용
class Solution:
    def isPalindrome_2(self, head: ListNode) -> bool:
        # head에서 출발해 2칸씩 이동하는 fast와 1칸씩 이동하는 slow
        slow = fast = head
        # head의 역순 연결리스트인 rev 작성
        rev = None
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next 

        # head의 길이가 홀수
        if fast:
            slow = slow.next
        
        # 절반 지점에 도착해있는 slow는 head의 오른쪽으로, rev는 왼쪽으로 이동하며 비교하는 것과 같음
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        
        return not rev

head = [1,2,2,1]
print(isPalindrome_2(head))