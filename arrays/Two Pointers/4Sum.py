class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        if len(nums)<4: return []
        nums.sort()
        n=len(nums)
        s=set()

        for p0 in range(n):
            if p0 > 0 and nums[p0] == nums[p0 - 1]: continue

            for p1 in range(p0+1,n):
                if p1 > p0 + 1 and nums[p1] == nums[p1 - 1]: continue
                p2,p3=p1+1,n-1         #keeping two no. fixed and iterating 2 movable no.s

                while p2<p3:
                    total = nums[p0]+nums[p1]+nums[p2]+nums[p3]

                    if total==target:
                        s.add((nums[p0],nums[p1],nums[p2],nums[p3]))
                        p2+=1
                        p3-=1
                    elif total<target: p2+=1
                    else: p3-=1
        
        return list(s)
