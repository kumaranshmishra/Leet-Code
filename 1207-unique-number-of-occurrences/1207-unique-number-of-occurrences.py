class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        x = set()
        for i in set(arr):
            if arr.count(i) in x:
                return False
            a = arr.count(i)    
            x.add(a)
        return True        
        