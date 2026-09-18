class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        import math
        n=len(nums)
        l=[1]*n
        prod=1

        for x in range(n):            
            l[x]=prod
            prod*=nums[x]
        
        prod1=1
        for x in range(n-1,-1,-1):
            l[x]*=prod1
            prod1*=nums[x]
                    
        return l        
