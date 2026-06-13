class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = 1

        totalPaths = m + n - 2

        r = min(m-1, n-1)

        for i in range(1, r + 1):
            paths = paths * (totalPaths - r + i) // i

        return int(paths)