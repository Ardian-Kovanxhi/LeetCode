class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            if stack and temp > stack[-1][0]:
                while stack and temp > stack[-1][0]:
                    curr = stack.pop()
                    ans[curr[1]] = i - curr[1]
            stack.append((temp,i))
                
        return ans