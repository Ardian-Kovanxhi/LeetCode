class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0
        for i in range(n - 1, -1, -1):
            j = m - 1
            while j != -1 and grid[i][j] < 0:
                ans += 1
                j -= 1
        return ans