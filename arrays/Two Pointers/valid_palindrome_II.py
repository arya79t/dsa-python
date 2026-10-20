class Solution:
    def validPalindrome(self, s: str) -> bool:
        left,right=0,len(s)-1
        
        while left<right:
            if s[left]==s[right]: #both outer match or not
                left+=1
                right-=1                
            else:         #abcaba -> ca
               return s[left+1:right+1]==s[left+1:right+1][::-1] or s[left:right]==s[left:right][::-1] #if remaining characters after removing form a palindrome like ca -> a or ca -> c
        
        return True  #if it stops at aba -> b
