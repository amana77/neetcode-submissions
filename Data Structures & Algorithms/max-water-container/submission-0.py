class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxa=0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                maxa=max(maxa,(j-i)*min(heights[i],heights[j]))
        return maxa