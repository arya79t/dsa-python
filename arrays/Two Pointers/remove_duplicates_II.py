class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k=0

        for x in nums:
            if k<2 or x!=nums[k-2]: #Python does not evaluate right side.
                nums[k]=x           #Thus, nums[-2] is never accessed!
                k+=1                
        
        return k
