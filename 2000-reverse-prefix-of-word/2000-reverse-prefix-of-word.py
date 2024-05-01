class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        post = ""
        for i, v in enumerate(word):
            if v == ch:
                post = word[i + 1:]
                for ind in range(i + 1):
                    post = word[ind] + post
                return post
        return word