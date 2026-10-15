class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        m=-1

        for x in range(len(arr)-1,-1,-1):
            c=arr[x]
            arr[x]=m
            m=m if m>c else c
        
        return arr
