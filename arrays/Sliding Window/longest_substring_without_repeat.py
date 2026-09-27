class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,m,sub=0,0,set()

        for right in range(len(s)):            
            
            while s[right] in sub:
                sub.remove(s[left])
                left+=1                
            
            sub.add(s[right])
            if len(sub)>m:m=len(sub)
        
        return m
