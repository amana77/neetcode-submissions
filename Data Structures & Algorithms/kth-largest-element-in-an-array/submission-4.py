class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        t=len(nums)-k
        def partition(l,r):
            i,j=l,r
            pivot=nums[l]
            while True:
                while nums[i]<=pivot and i<r:
                    i+=1
                while nums[j]>=pivot and j>l:
                    j-=1
                if i>=j:
                    break
                nums[i],nums[j]=nums[j],nums[i]
            nums[j],nums[l]=nums[l],nums[j]
            return j
        def quickselect(l,r):
            j=partition(l,r)
            if j>t:
                return quickselect(l,j-1)
            elif j<t:
                return quickselect(j+1,r)
            else:
                return nums[j]  
        return quickselect(0,len(nums)-1)