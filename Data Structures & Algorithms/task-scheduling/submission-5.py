class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=[0]*26
        for t in tasks:
            count[ord(t)-ord('A')]+=1
        m=max(count)
        maxcount=0
        for i in count:
            maxcount += 1 if i==m else 0
        t=(m-1)*(n+1)+maxcount
        return max(t,len(tasks))