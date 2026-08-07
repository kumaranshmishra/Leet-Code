class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        maps = {}
        mapt = {}
        for i in range(len(s)):
            if s[i] not in maps:
                maps[s[i]] = t[i]
            if t[i] not in mapt:
                mapt[t[i]] = s[i]

            if maps[s[i]] != t[i] or mapt[t[i]] != s[i]:
                return False
        return True