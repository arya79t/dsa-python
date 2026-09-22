class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:        
        current=sum(nums[:k])
        m=current

        for x in range(k,len(nums)):
            current+=nums[x]-nums[x-k]
            if current>m: m=current
        
        return m/k
