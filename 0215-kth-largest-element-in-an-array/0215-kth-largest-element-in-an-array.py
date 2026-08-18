import heapq as h
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        for i in range (len(nums)):
            nums[i] = -nums[i]
        h.heapify(nums)
        while k!=0 :
            m = -h.heappop(nums)
            k = k-1
        return m        

        