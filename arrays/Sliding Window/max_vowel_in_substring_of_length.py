class Solution:
    def maxVowels(self, s: str, k: int) -> int:        
        current=sum([1 for x in s[0:k] if x in 'aeiou'])
        m=current

        for x in range(k,len(s)):
            current-=1 if s[x-k] in 'aeiou' else 0

            if s[x] in 'aeiou': current+=1
            if current>m:m=current            
        
        return m
