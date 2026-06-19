class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=defaultdict(int)
        out=[]
        for n in nums:
            count[n]+=1
        list_count=sorted(count,key=count.get,reverse=True)
        for i in range(k):
            out.append(list_count[i])
        return out          