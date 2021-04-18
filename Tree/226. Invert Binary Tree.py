class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # head같은걸로 안 가리켜도 되나... 헷갈리는데 어쨌든 됨..
    def invertTree_1(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
    
    # 반복을 이용한 풀이
    def invertTree_2(self, root: TreeNode) -> TreeNode:
        q = collections.deque([root])

        while q:
            node = q.popleft()
            if node:
                node.left, node.right = node.right, node.left
                q.append(node.left)
                q.append(node.right)
        
        return root