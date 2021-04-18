class Solution:
    longest: int = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(root):
            if root is None:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            self.longest = max(self.longest, left + right + 2)
            return 1 + max(left, right)
        
        dfs(root)
        return self.longest