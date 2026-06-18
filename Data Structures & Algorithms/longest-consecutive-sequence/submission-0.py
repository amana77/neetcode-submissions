class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sets=set(nums)
        longest=0
        for n in nums:
            if n-1 not in sets:
                curr_len=1
                curr_num=n
                while curr_num+1 in sets:
                    curr_len+=1
                    curr_num+=1
                longest=max(longest,curr_len)
        return longest