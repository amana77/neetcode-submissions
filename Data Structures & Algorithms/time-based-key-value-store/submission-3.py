class TimeMap:

    def __init__(self):
        self.tmap={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.tmap:
            self.tmap[key].append((timestamp,value))
        else:
            self.tmap[key]=[(timestamp,value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tmap:
            return ''
        arr=self.tmap[key]
        l,r=0,len(arr)-1
        res=''
        while l<=r:
            m=(l+r)//2
            if timestamp<arr[m][0]:
                r=m-1
            else:
                l=m+1
                res=arr[m][1]
        return res
        
