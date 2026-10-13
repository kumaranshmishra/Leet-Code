class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        res = []
        for i in range(len(nums)):
            s = target-nums[i]
            if s in nums:
                x = nums.index(s) 
                if x != i:
                    return [i,x]    
        return res           