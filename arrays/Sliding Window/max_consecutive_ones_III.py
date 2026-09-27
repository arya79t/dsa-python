class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left,curr,max_sub=0,0,0

        for right in range(len(nums)):
            if nums[right]==0: curr+=1

            while curr>k:
                if nums[left]==0: curr-=1
                left+=1

            if right-left+1>max_sub: max_sub=right-left+1                
        
        return max_sub     
