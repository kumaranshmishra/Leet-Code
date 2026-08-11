class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = {}

        for ch in s:
            if ch not in res:
                res[ch] = 1
            else:
                res[ch] += 1

        for ch in t:
            if ch not in res:
                return ch

            res[ch] -= 1

            if res[ch] < 0:
                return ch