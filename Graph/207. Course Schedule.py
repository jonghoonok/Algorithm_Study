import collections

# 풀이1: Topology Sort를 이용
def canFinish_1(numCourses: int, prerequisites) -> bool:
    
        indegree = [0]*numCourses
        courses = [[] for _ in range(numCourses)]

        for pre in prerequisites:
            courses[pre[1]].append(pre[0])
            indegree[pre[0]] += 1

        q = deque()

        for i in range(numCourses):
            if not courses[i]:
                q.append(i)
                break
        
        while q:
            t = q.popleft()
            for node in courses[t]:
                indegree[node] -= 1
                if not indegree[node]:
                    q.append(node)

        for node in indegree:
            if node:
                return False
        
        return True


# 풀이2: DFS
def canFinish_2(numCourses: int, prerequisites) -> bool:
    courses = collections.defaultdict(list)
    for pre in prerequisites:
        courses[pre[0]].append(pre[1])

    # 사이클을 형성하는지 DFS를 이용하여 판별
    loop = set()
    def dfs(node):
        if node in loop:
            return False
        
        loop.add(node)
        for course in courses[node]:
            if not dfs(course):
                return False
        loop.remove(node)
        return True

    for course in list(courses):
        if not dfs(course):
            return False
    return True


# 풀이3: 가지치기
def canFinish_3(numCourses: int, prerequisites) -> bool:
    courses = collections.defaultdict(list)
    for pre in prerequisites:
        courses[pre[0]].append(pre[1])

    # 사이클을 형성하는지 DFS를 이용하여 판별
    loop = set()
    visited = set()
    def dfs(node):
        if node in loop:
            return False
        # 이미 방문했던 노드이면 True
        if node in visited:
            return True
        
        loop.add(node)
        for course in courses[node]:
            if not dfs(course):
                return False
        loop.remove(node)
        # 사이클 없음이 확인됐으면 방문 노드에 추가
        visited.add(node)
        return True

    for course in list(courses):
        if not dfs(course):
            return False
    return True
    
print(canFinish_2(5, [[1,4],[2,4],[3,1],[3,2]]))