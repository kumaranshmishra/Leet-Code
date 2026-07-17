class Solution(object):
    def maximumWealth(self, accounts):
        max1 = 0
        for i in range(len(accounts)):
            high = 0 
            for j in range(len(accounts[i])):
                high = high + accounts[i][j]  
            if max1 < high:
                max1 = high
        return max1