class Solution(object):
    def canJump(self, nums):
        farthest = 0

        for i in range(len(nums)):

            if i > farthest:
                return False

            if i + nums[i] > farthest:
                farthest = i + nums[i]

        return True