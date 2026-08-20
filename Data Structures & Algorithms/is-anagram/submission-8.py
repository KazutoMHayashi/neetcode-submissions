class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_split = sorted([x for x in s])
        t_split = sorted([x for x in t])

        if s_split == t_split:
            return True
        return False
