class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        t=0
        count=Counter(tasks)
        maxheap=[-c for c in count.values()]
        heapq.heapify(maxheap)
        while maxheap:
            i=0
            temp=[]
            while i<=n:
                t+=1
                if maxheap:
                    nums=heapq.heappop(maxheap)
                    nums+=1
                    if nums<0:
                        heapq.heappush(temp,nums)
                if not temp:
                    break
                i+=1
            for v in temp:
                heapq.heappush(maxheap,v)
        return t
            
            