class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        
        # edge: b -> a
        for a, b in prerequisites:
            graph[b].append(a)

        state = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = done

        def dfs(course: int) -> bool:
            if state[course] == 1:
                return False  # cycle found
            if state[course] == 2:
                return True   # already checked, no cycle

            state[course] = 1  # mark as visiting

            for nxt in graph[course]:
                if not dfs(nxt):
                    return False

            state[course] = 2  # mark as done
            return True

        for course in range(numCourses):
            if state[course] == 0:
                if not dfs(course):
                    return False

        return True