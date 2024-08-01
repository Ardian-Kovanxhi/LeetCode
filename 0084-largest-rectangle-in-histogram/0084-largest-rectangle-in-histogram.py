class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []

        largest = 0

        for i, v in enumerate(heights):
            start = i
            while stack and v < stack[-1][1]:
                index, height = stack.pop()
                largest = max(largest, (height * (i - index)))
                start = index
            stack.append((start,v))
        while stack:
            index, height = stack.pop()
            largest = max(largest, (height * (len(heights) - index)))
        return largest