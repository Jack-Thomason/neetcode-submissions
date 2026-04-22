class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        # Build graph and indegree array
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        # Start with courses having no prerequisites
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        taken = 0

        while q:
            course = q.popleft()
            taken += 1

            for nxt in graph[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        return taken == numCourses