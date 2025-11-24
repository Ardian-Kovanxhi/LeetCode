class Codec:
    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings to a single string.
        """
        if not strs:
            return ""
        lengths = []
        for s in strs:
            lengths.append(str(len(s)) + ",")
        return "".join(lengths) + "#" + "".join(strs)

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string to a list of strings.
        """
        if not s:
            return []
        sizes, ans, i = [], [], 0
        while s[i] != "#":
            curr = ""
            while s[i] != ",":
                curr += s[i]
                i += 1
            sizes.append(int(curr))
            i += 1
        i += 1

        for size in sizes:
            ans.append(s[i : i + size])
            i += size
        return ans
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))