# 풀이1: 재귀로 간단히 풀었는데 상당히 느림
def maxDepth_1(root) -> int:
    if root is None:
        return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# 풀이2: 나름 가지치기를 하려고 했으나 역시 느림
def maxDepth_2(root) -> int:
        if root is None:
            return 0
        def dfs(root):
            if root.left is None:
                if root.right is None:
                    return 1 + max(dfs(root.left), dfs(root.right))
                else:
                    return 1 + dfs(root.right)
            else:
                if root.right is None:
                    return 1 + dfs(root.left)
                else:
                    return 1
        return dfs(root)

# BFS
def maxDepth_3(root) -> int:
        if root is None:
            return 0

        q = collections.deque([root])
        depth = 0

        while q:
            depth += 1
            for _ in range(len(q)):
                t = q.popleft()
                if t.left is not None:
                    q.append(t.left)
                if t.right is not None:
                    q.append(t.right)
        
        return depth
