class Solution:
    def findMin(self, nums: list[int]) -> int:
        left,right=0,len(nums)-1

        while left<right:
            mid=(left+right)//2        

            if nums[mid]>nums[right]: left=mid+1 #since smaller elements are always to the right in rotation
            else: right=mid
        
        return nums[right]
