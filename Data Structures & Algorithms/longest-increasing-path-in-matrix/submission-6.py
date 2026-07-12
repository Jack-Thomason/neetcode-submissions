class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        indegree = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                
                    if (
                        0 <= ni < m
                        and 0 <= nj < n
                        and matrix[ni][nj] < matrix[i][j]
                    ):
                        indegree[i][j] += 1
        
        queue = deque()

        for i in range(m):
            for j in range(n):
                if indegree[i][j] == 0:
                    queue.append((i, j))

        path_length = 0

        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()

                for di, dj in directions:
                    ni, nj = i + di, j + dj

                    if(
                        0 <= ni < m
                        and 0 <= nj < n
                        and matrix[ni][nj] > matrix[i][j]

                    ):
                        indegree[ni][nj] -= 1

                        if indegree[ni][nj] == 0:
                            queue.append((ni, nj))

            path_length += 1
        
        return path_length