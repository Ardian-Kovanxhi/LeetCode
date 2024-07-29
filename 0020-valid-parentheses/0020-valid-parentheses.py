class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for ch in s:
            if ch not in Map: 
                stack.append(ch)
                continue
            elif not stack or stack[-1] != Map[ch]: 
                return False
            else: stack.pop()
        return not stack