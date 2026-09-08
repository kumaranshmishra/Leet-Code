class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = nums1+nums2
        x.sort()
        if len(x)%2==0:
            ans = (x[len(x)//2-1] +  x[len(x)//2]) /2
            return ans
        else :
            ans = x[len(x)//2]    
            return ans

















        