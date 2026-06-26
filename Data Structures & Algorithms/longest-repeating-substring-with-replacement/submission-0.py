class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        for i in range(len(s)):
            count={}
            for j in range(i,len(s)):
                count[s[j]]=count.get(s[j],0)+1
                maxc=max(count.values())
                if (j-i+1)-maxc<=k:
                    res=max(res,j-i+1)
        return res
