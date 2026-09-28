class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left=0
        current=0
        m=float('inf')

        for right in range(len(nums)):
            current+=nums[right]

            while current>=target:   
                if right-left+1<m: m=right-left+1

                current-=nums[left]
                left+=1            
        
        if m==float('inf'): return 0
        return m 
