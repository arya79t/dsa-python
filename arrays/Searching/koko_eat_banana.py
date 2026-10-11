class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        import math # / rounds down value

        left,right=1,max(piles)

        while left<right:
            k=(left+right)//2
            hours=0

            for pile in piles:
                hours+=math.ceil(pile/k) #rounds up value
            
            if hours<=h: 
                right=k # This speed works; try slower
            else: left=k+1 # Need a faster speed
        
        return left #or we can return right
