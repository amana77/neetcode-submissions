class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_dict={}
        for i,n in enumerate(numbers):
            diff=target-n
            num_dict[n]=i
            if diff in num_dict.keys() and n!=diff:
                return [num_dict[diff]+1,i+1]