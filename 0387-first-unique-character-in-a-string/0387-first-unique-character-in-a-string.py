class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = {}
        for i in s :
            if i not in res :
                 res[i] = 1 
            else :
                res[i] += 1
        for i in range(len(s)):
            if res[s[i]] == 1:
                return i
        return -1                

           
