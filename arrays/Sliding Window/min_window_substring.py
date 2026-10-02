class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d1,d2={},{}
        form,left=0,0        
        min_s=(0,len(s))
        found=False

        for x in t:
            if x not in d1: d1[x]=1
            else: d1[x]+=1
        
        req=len(d1)
        
        for x in range(len(s)):
            if s[x] not in d2: d2[s[x]]=1
            else: d2[s[x]]+=1

            if s[x] in d1 and d2[s[x]]==d1[s[x]]: form+=1
                            
            while form==req:
                found=True
                min_s=min(min_s,(left,x),key=lambda y: y[1]-y[0]+1)

                d2[s[left]]-=1
                if d2[s[left]]==0: del d2[s[left]]

                if s[left] in d1 and d2.get(s[left],0)<d1[s[left]]: form-=1
                left+=1
        
        if not found: return ""
        return s[min_s[0]:min_s[1]+1]
