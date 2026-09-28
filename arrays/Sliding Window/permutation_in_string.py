class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2): return False

        d1,d2={},{}
        l_s1=len(s1)        

        for x in range(l_s1):
            if s1[x] not in d1: d1[s1[x]]=1
            else: d1[s1[x]]+=1

            if s2[x] not in d2: d2[s2[x]]=1
            else: d2[s2[x]]+=1

        if d1==d2:return True

        for right in range(l_s1,len(s2)):
            d2[s2[right-l_s1]]-=1
            if d2[s2[right-l_s1]]<=0: del d2[s2[right-l_s1]]

            if s2[right] not in d2: d2[s2[right]]=1
            else: d2[s2[right]]+=1
            
            if d1==d2: return True
        
        return False
