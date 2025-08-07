class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        l, r = 0, 0
        baskets = {}

        for r in range(n):
            continue