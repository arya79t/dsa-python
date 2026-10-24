class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        p1,p2=len(s)-1,len(t)-1
        skip_s=skip_t=0

        while p1 >-1 or p2 >-1:
            if p1>-1 and s[p1]=='#':
                skip_s+=1
                p1-=1
            elif p1>-1 and skip_s>0:
                skip_s-=1
                p1-=1
            elif p2>-1 and t[p2]=='#':
                skip_t+=1
                p2-=1
            elif p2>-1 and skip_t>0:
                skip_t-=1
                p2-=1
            else:
                if p1>-1 and p2>-1:
                    if s[p1]!=t[p2]: return False
                elif p1>-1 or p2>-1: return False

                p1-=1
                p2-=1

        return True
