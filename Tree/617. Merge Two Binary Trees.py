class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees_1(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 is None:
            if root2 is None:
                return None
            else:
                return root2
        else:
            if root2 is None:
                return root1
            else:
                root1.val += roo2.val
                root1.left = self.mergeTrees(root1.left, roo2.left)
                root1.right = self.mergeTrees(root1.right, roo2.right)
                return root1

    # 똑같은 풀이긴한데 코드가 간결해지니 참고하자
    def mergeTrees_2(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees_2(root1.left, root2.left)
            node.right = self.mergeTrees_2(root1.right, root2.right)
            return node
        else:
            # Short-circuit evaluation 이용해서 코드 단축
            return root1 or root2