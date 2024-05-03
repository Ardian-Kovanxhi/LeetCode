class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        diff = 0

        i = 0

        while i < len(v1) or i < len(v2):
            tmp1 = int(v1[i]) if i < len(v1) else 0
            tmp2 = int(v2[i]) if i < len(v2) else 0

            if tmp1 != tmp2:
                diff = 1 if tmp1 > tmp2 else -1
                break
            i += 1
        return diff