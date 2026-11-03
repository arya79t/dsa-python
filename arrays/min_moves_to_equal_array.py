class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return max(nums) * len(nums) - sum(nums) 

        """Eg. (9-7)+(9-2)+(9-9)+(9-4)
        Expanding: =9+9+9+9-(7+2+9+4)
        Taking common terms: =(9*4)-22 (sum)"""
