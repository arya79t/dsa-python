class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        p=0
        for x in range(1,len(nums)):
            if nums[x]!=nums[p]: 
                nums[p+1]=nums[x]
                p+=1
        return p+1
