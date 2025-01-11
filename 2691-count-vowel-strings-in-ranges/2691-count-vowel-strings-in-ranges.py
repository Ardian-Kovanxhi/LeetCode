class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        vowels = {"a", "e", "i", "o", "u"}
        prefix = [0] * (n + 1)

        for i in range(n):
            curr = words[i]
            if curr[0] in vowels and curr[-1] in vowels:
                prefix[i + 1] = prefix[i] + 1
            else:
                prefix[i + 1] = prefix[i]

        ans = []
        for query in queries:
            ans.append(prefix[query[1] + 1] - prefix[query[0]])

        return ans