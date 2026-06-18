class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups=defaultdict(list)
        for ele in strs:
            sorted_ele=''.join(sorted(ele))
            groups[sorted_ele].append(ele)
        return list(groups.values())

