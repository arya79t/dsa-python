class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        l1,l2=len(nums1),len(nums2)
        p1,p2=0,0
        l=[]
        
        while p1<l1 or p2<l2:
            if p1>=l1: 
                l.append(nums2[p2])
                p2+=1
            elif p2>=l2:
                l.append(nums1[p1])
                p1+=1
            elif nums1[p1][0]==nums2[p2][0]: 
                l.append([nums1[p1][0],nums1[p1][1]+nums2[p2][1]])
                p1+=1
                p2+=1
            elif nums1[p1][0]<nums2[p2][0]: 
                l.append(nums1[p1])
                p1+=1
            else: 
                l.append(nums2[p2])  
                p2+=1          
        
        return l
