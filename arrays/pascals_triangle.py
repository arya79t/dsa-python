class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        l=[[1]]

        for x in range(1,numRows):
            el=[1]*(x+1)
            for y in range(1,x+1):                
                if y!=x: el[y]=l[x-1][y-1]+l[x-1][y] #for boundary
            
            l.append(el)
        
        return l
