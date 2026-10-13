class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        from collections import defaultdict
        d=defaultdict(list)

        for x in strs:
            s=''.join(sorted(x))
            d[s].append(x)
        
        return list(d.values())        
