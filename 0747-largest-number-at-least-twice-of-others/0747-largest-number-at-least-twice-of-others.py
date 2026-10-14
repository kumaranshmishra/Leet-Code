class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        x = max(nums)
        for i in range (len(nums)):
            if nums[i]!= x and nums[i]*2 > x:
                return -1 
        return nums.index(x)        
        