class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        c,left,right=0,[],[]
        for x in nums:
            if x<pivot: left.append(x)
            elif x==pivot: c+=1
            else: right.append(x)
        
        return left + [pivot]*c + right
