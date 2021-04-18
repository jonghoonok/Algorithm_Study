class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def depth(node):
            if node is None:
                return 0
            
            left = depth(node.left)
            right = depth(node.right)

            # 높이 차이가 없으면 1씩 증가, 있으면 -1
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return check(root) != -1