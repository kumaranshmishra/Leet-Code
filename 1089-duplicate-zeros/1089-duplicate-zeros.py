class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        res = []
        for i in range(len(arr)):
            if arr[i] == 0:
                res.append(0)
                res.append(0)
            else:
                res.append(arr[i])
        arr[:] = res[:len(arr)]        
        