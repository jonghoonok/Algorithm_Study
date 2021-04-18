class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    result = 0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        def dfs(node):
            left, right = 0, 0
            if node.left:
                left = dfs(node.left)
                left = left + 1 if node.left.val == node.val else 0
            if node.right:
                right = dfs(node.right)
                right = right + 1 if node.right.val == node.val else 0
            
            self.result = max(self.result, left+right)

            return max(left, right)
        
        dfs(root)
        return result