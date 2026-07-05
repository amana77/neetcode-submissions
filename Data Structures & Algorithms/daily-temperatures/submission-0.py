class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[]
        for i in range(len(temperatures)):
            flag=False
            for j in range(i,len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    result.append(j-i)
                    flag=True
                    break
            if flag==False:
                result.append(0)
        return result
