class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1

        while top <= bot:
            mid = (top + bot) // 2
            row = matrix[mid]

            if target > row[-1]: top = mid + 1
            elif target < row[0]: bot = mid - 1
            else: break
        
        if not (top <= bot):
            return False
        
        row = matrix[(top + bot) // 2]
        l = 0
        r = cols - 1
        while l <= r:
            mid = (l + r) // 2
            midVal = row[mid]

            if midVal == target: return True
            elif midVal < target: l = mid + 1
            else: r = mid - 1
        return False