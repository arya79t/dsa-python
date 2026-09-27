class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        f={}
        left,max_sub=0,0

        for right in range(len(s)):
            if s[right] in f: f[s[right]]+=1
            else: f[s[right]]=1

            replace=right-left+1-max(f.values())

            while replace>k:
                f[s[left]]-=1
                left+=1
                replace-=1

            if right-left+1>max_sub:max_sub=right-left+1
        
        return max_sub
