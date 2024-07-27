class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for word in strs:
            hashkey = [0] * 26

            for char in word:
                hashkey[ord(char) - ord("a")] += 1
            
            ans[tuple(hashkey)].append(word)
        print(ans)
        
        return ans.values()