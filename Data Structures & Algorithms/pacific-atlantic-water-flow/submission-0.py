class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []


        rows, cols = len(heights), len(heights[0])
        atlantic = set()
        pacific = set()

        def dfs(r: int, c: int, visited: set):
            visited.add((r, c))

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows and
                    0 <= nc < cols and 
                    heights[nr][nc] >= heights[r][c] and
                    (nr, nc) not in visited
                ):
                    dfs(nr, nc, visited)


        



        for c in range(cols):
            dfs(0, c, pacific)
        for r in range(rows):
            dfs(r, 0, pacific)

        for c in range(cols):
            dfs(rows - 1, c, atlantic)
        for r in range(rows):
            dfs(r, cols - 1, atlantic)
        
        return [[r, c] for (r, c) in pacific & atlantic]
