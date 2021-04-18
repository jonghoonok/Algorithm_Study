def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # 연결된 노드가 하나뿐인 노드(리프 노드)를 leaf에 추가
        leaf = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaf.append(i)

        while n > 2:
            n -= len(leaf)
            new_leaf = []
            for node in leaf:
                parent = graph[node].pop()
                graph[parent].remove(node)

                if len(graph[parent]) == 1:
                    new_leaf.append(parent)
            
            leaf = new_leaf

        return leaf