class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree_1(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            root = TreeNode(preorder[0])
            mid = inorder.index(root.val)
            root.left = self.buildTree_1(preorder[1:mid+1], inorder[:mid]) 
            root.right = self.buildTree_1(preorder[mid+1:], inorder[mid+1:]) 
            return root
    

    # 책의 풀이: pop을 쓰는데 어째선지 내 풀이보다 빠르다..
    def buildTree_2(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            index = inorder.index(preorder.pop(0))
            
            root = TreeNode(inorder[index])
            root.left = self.buildTree_2(preorder, inorder[:index]) 
            root.right = self.buildTree_2(preorder, inorder[index+1:]) 
            return root