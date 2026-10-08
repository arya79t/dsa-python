class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left,right=0,len(nums)-1

        while left<=right:
            mid=(left+right)//2

            if nums[mid]==target: return mid
            elif nums[mid]>=nums[right] and nums[mid]<target<=nums[right]: left=mid+1 #left half> right half: search in right half
            elif nums[left]<=nums[mid] and nums[mid]<target<=nums[right]: left=mid+1 #search in right half
            else: right=mid-1
        
        return -1
