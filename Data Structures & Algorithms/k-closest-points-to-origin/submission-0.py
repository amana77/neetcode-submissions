class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d_dict={}
        dist=[]
        res=[]
        for p in points:
            d=(p[0])**2 + (p[1])**2
            if d not in d_dict.keys():
                d_dict[d]=[p]
            else:
                d_dict[d].append(p)
            dist.append(d)
        dist.sort()
        for i in range(k):
            res.append(d_dict[dist[i]].pop())
        return res