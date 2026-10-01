class Solution:
    def maxProduct(self, n: int) -> int:
        digits = []

        while n:
            rem = n % 10
            digits.append(rem)
            n = n // 10

        digits.sort()

        return digits[-1] * digits[-2]