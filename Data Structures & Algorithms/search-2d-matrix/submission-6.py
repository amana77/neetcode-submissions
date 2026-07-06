class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r=0,len(matrix)*len(matrix[0])-1
        while l<=r:
            m=(l+r)//2
            row,c=m//len(matrix[0]),m%len(matrix[0])
            if target > matrix[row][c]:
                l = m + 1
            elif target < matrix[row][c]:
                r = m - 1
            else:
                return True
        return False