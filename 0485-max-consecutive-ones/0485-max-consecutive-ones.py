class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        fin = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                if count > fin:
                    fin = count
                count = 0

        if count > fin:
            fin = count

        return fin