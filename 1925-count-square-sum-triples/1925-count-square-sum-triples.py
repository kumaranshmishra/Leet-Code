class Solution:
    def countTriples(self, n: int) -> int:
        return sum(isqrt(c2:=a*a+b*b)**2==c2<=n*n
            for a,b in combinations(range(1,n+1),2))*2