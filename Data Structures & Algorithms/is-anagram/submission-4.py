class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_con=''.join(sorted(s))
        t_con=''.join(sorted(t))
        return s_con==t_con 