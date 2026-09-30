class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        d={}
        left,max_f,current=0,0,0
        
        for right in range(len(fruits)):
            if fruits[right] not in d: d[fruits[right]]=1
            else: d[fruits[right]]+=1
            current+=1

            if len(d)>2:                                        
                current-=1
                d[fruits[left]]-=1
                if d[fruits[left]]==0: del d[fruits[left]]
                left+=1
            
            if current>max_f: max_f=current
        
        return max_f
