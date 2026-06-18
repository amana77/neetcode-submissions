class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag=False
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]==nums[i]:
                    flag=True
                    break
        return flag
                
