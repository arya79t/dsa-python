class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left=0
        total=0
        min_w=float('inf')
        
        for right in range(len(nums)):
            total+=nums[right]

            while total>= target:
                if right-left+1<min_w: min_w=right-left+1

                total-=nums[left]
                left+=1

        if min_w==float('inf'): return 0
        return min_w
