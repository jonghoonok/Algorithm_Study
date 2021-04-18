class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    val: int = 0
    def bstToGst_1(self, root: TreeNode) -> TreeNode:
        # 트리의 모든 노드의 합을 먼저 구함
        def get_sum(node):
            if node is None:
                return 0
            return get_sum(node.left) + node.val + get_sum(node.right)

        # 구한 합을 이용해서 트리의 원소들을 교체해줌
        def sum_tree(node, down):
            if node is None:
                return 0

            # 원래 노드의 값
            mid = node.val
            # 왼쪽으로 내려갈 때는 위에서 내려온 값을 그대로 내림
            left = sum_tree(node.left, down)
            # 위에서 내려온 값 down에서 자기보다 왼쪽에 있는 서브트리의 합 left를 빼줌
            node.val = down - left
            # 오른쪽으로 갈 때는 갱신된 값 node.val에서 원래 자신의 값 mid를 빼서 내려줌
            right = sum_tree(node.right, node.val - mid)

            # 자신을 포함한 서브트리의 합을 리턴: 위에서 left로 받아서 빼야 함
            return left + mid + right

        sum_tree(root, get_sum(root))
        return root
    

    # 책의 풀이: 오른쪽-부모-왼쪽 순서로 중위 순회
    def bstToGst_2(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst_2(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst_2(root.left)
        return root