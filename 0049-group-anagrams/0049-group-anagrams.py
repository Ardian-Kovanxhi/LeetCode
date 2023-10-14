class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashLogger = {}

        for str in strs:
            hash = [0] * 26

            for s in str:
                hash[ord(s) - 97] += 1
            
            temp = tuple(hash)

            if temp in hashLogger:
                hashLogger[temp].append(str)
            else:
                hashLogger[temp] = [str]
        return hashLogger.values()