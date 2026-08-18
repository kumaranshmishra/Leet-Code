import heapq as h
class Solution(object):
    def findKthLargest(self, nums, k):
        for i in range (len(nums)):
            nums[i] = -nums[i]
        h.heapify(nums)
        while k!=0 :
            m = -h.heappop(nums)
            k = k-1
        return m        

        