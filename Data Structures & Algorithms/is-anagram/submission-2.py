class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_con=''.join(sorted(s))
        t_con=''.join(sorted(t))
        if s_con==t_con:
            return True
        return False