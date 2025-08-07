class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        l = 0

        for right, fruit in enumerate(fruits):
            basket[fruit] = basket.get(fruit, 0) + 1

            if len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l += 1

        return right - l + 1