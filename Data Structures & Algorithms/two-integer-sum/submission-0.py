class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        List=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sum=nums[i]+nums[j]
                if sum==target:
                    List.extend([i,j])
                    return List