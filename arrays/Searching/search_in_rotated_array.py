class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left,right=0,len(nums)-1

        while left<=right:
            mid=(left+right)//2

            if nums[mid]==target: return mid
            elif nums[mid]<=nums[right] and nums[mid]<target<=nums[right]: left=mid+1 # Right half is sorted
            elif nums[mid]<=nums[right]: right=mid-1 # Right half is sorted, target is not there
            elif nums[left]<=nums[mid] and nums[left]<=target<nums[mid]: right=mid-1 # Left half is sorted and target in left
            else: left=mid+1
        
        return -1
