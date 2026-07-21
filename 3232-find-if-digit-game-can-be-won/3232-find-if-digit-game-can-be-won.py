class Solution(object):
    def canAliceWin(self, nums):
        alice = 0
        bob = 0

        for i in range(len(nums)):
            if nums[i] < 10:
                alice = alice + nums[i]
            else:
                bob = bob + nums[i]

        if alice != bob:
            return True
        return False