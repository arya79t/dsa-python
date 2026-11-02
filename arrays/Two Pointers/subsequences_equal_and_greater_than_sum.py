class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        nums.sort()
        left,right=0,len(nums)-1
        sub=0

        while left<=right:
            if nums[left]+nums[right]>target: right-=1
            else:
                sub+=2**(right-left)
                left+=1
        
        return sub%(10**9+7)
