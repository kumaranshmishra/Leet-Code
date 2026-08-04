class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        a = max(nums)
        b = min(nums)
        for i in range (b , a):
            if i not in nums:
               res.append(i)
        return res       
            