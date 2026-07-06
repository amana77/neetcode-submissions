class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r=0,len(matrix)-1
        while l<=r:
            m=(r+l)//2
            if matrix[m][0]==target:
                return True
            elif matrix[m][0]>target:
                r=m-1
            elif matrix[m][0]<target:
                if m==len(matrix)-1 or target<matrix[m+1][0]:
                    break
                else:
                    l=m+1
        l,r=0,len(matrix[m])-1
        while l<=r:
            e=(r+l)//2
            if matrix[m][e]==target:
                return True
            elif matrix[m][e]>target:
                r=e-1
            elif matrix[m][e]<target:
                l=e+1
        return False