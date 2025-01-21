class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        preR1, preR2 = grid[0].copy(), grid[1].copy()

        for i in range(1, n):
            preR1[i] += preR1[i - 1]
            preR2[i] += preR2[i - 1]

        res = float("inf")
        for i in range(n):
            top = preR1[-1] - preR1[i]
            bottom = preR2[i - 1] if i > 0 else 0
            secondRobot = max(top, bottom)
            res = min(secondRobot, res)
        return res