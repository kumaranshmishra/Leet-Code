class Solution(object):
    def intersection(self, nums1, nums2):
        a = []
        for i in nums1:
            if i in nums2:
                a.append(i)
        return list(set(a)) 
