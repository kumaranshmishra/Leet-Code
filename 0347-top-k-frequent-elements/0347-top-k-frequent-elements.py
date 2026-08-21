import heapq as hq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}

        for i in range(len(nums)):
            res[nums[i]] = res.get(nums[i], 0) + 1
        
        return hq.nlargest(k, res.keys(), key=res.get)    
