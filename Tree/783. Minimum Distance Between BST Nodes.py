class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    prev: int = -100000
    result: int = 100000
    # 중위 순회를 이용
    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)

        # 왼쪽 서브트리의 가장 오른쪽 값 prev와 현재 값의 차와 result를 비교하여 갱신
        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.result