# Move all zeros to the end while maintaining the order of non-zero elements.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos = 0

        for x in range(len(nums)):
            if nums[x] != 0:
                nums[pos], nums[x] = nums[x], nums[pos]
                pos += 1
"""
Approach:
Use a pointer `pos` to track the position where the next non-zero element should go.

Time Complexity: O(n)
Space Complexity: O(1)
"""
