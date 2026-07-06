class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res=max(piles)
        l,r=1,res
        while l<=r:
            k=(l+r)//2
            e=0
            for b in piles:
                e-=(-b//k)
            if e<=h:
                r=k-1
                res=k
            elif e>h:
                l=k+1
        return res


            