class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix=''

        for x in range(len(strs[0])): #compare with the 1st value
            if all(x<len(y) and y[x]==strs[0][x] for y in strs): prefix+=strs[0][x]
            else: break
              
        return prefix
