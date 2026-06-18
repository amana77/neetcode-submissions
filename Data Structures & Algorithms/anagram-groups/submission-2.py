class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams={}
        for s in strs:
            s_con=''.join(sorted(s))
            if s_con in anagrams:
                anagrams[s_con].append(s)
            else:
                anagrams[s_con]=[s]
        return list(anagrams.values())