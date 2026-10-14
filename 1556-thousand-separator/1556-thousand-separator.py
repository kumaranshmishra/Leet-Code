
class Solution:
    def thousandSeparator(self, n: int) -> str:
        if len(str(n)) < 4:
            return str(n)

        count = 0
        res = ''
        s = str(n)
        x = len(s) - 1

        while x >= 0:
            if count == 3:
                res += '.'
                count = 0

            res += s[x]
            x -= 1
            count += 1

        return res[::-1]
