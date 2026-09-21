class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub=''        
        max_len=0

        for right in range(len(s)):
            while s[right] in sub:
                sub=sub[1:]
            
            sub+=s[right]
            if len(sub)>max_len: max_len=len(sub)
        
        return max_len
