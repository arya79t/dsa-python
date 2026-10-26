class Solution:
    def compress(self, chars: list[str]) -> int:
        if len(chars)==1: return 1
        p,c=0,1
        w=0 #write position

        for x in range(1,len(chars)):
            if chars[x]==chars[p]: c+=1
            else:
                chars[w]=chars[p] #storing the character to the position of write
                w+=1 #move next to store occurrence
                if c>1: 
                    sc=str(c)
                    for y in range(len(sc)):
                        chars[w]=sc[y]
                        w+=1
                c=1
                p=x
        
        chars[w]=chars[p]
        w+=1
        if c>1: 
            sc=str(c)
            for y in range(len(sc)):
                chars[w]=sc[y]
                w+=1
        return w
