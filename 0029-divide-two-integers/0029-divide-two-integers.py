class Solution(object):
    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        sign = 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1

        a = abs(dividend)
        b = abs(divisor)

        ans = 0

        while a >= b:
            num = b
            count = 1

            while a >= (num + num):
                num = num + num
                count = count + count

            a = a - num
            ans = ans + count

        return sign * ans