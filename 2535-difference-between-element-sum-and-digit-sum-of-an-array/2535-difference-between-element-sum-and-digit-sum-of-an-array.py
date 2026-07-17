class Solution(object):
    def differenceOfSum(self, nums):
        def array_sum(nums):
            total = 0
            for i in range(len(nums)):
                total += nums[i]
            return total
        
        def digit_sum(nums):
            total = 0
            for i in range(len(nums)):
                num = nums[i]
                while num > 0:
                    rem = num % 10
                    total += rem
                    num //= 10
            return total
        
        a = array_sum(nums)
        b = digit_sum(nums)
        return abs(a - b)