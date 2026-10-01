class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = 0
        temp = x
        while temp:
            rem = temp%10
            s = s+rem
            temp = temp//10
        if x%s == 0:
            return s
        else:
            return -1        
        