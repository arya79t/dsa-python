class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_s=0
        max_s=nums[0]

        for x in nums:
            if current_s<0:
                current_s=0
            
            current_s+=x
            max_s=max(current_s,max_s)
        
        return max_s     
