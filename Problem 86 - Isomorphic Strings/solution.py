class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_map = {}
        used = set()
        if len(s) == 1:
            return True
        for i in range(len(s)):
            if s[i] in hash_map:
                if hash_map[s[i]] != t[i]:
                    return False
            else:
                if t[i] in used:
                    return False
                used.add(t[i])
            hash_map[s[i]] = t[i]

        return True