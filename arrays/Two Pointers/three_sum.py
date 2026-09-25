class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        l=set()

        for x in range(len(nums)):
            p2,p3=x+1,len(nums)-1
            while p2<p3:
                s=nums[x]+nums[p2]+nums[p3]
                if s==0: 
                    l.add((nums[x],nums[p2],nums[p3]))
                    p2+=1
                    p3-=1
                elif s<0: p2+=1
                else: p3-=1

        return list(l)        
