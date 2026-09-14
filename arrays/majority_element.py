class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)//2
        d={}

        for x in nums:
            if x not in d: d[x]=1
            else: d[x]+=1

        return max(d, key=d.get)
