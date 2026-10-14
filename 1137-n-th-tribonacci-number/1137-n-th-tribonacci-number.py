class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <=2:
            return 1    
        b1 = 0
        b2 = 1
        b3 = 1
        res = 0
        for i in range(3,n+1):
            res = b1+b2+b3
            b1 = b2
            b2 = b3
            b3 = res
        return b3
             
        