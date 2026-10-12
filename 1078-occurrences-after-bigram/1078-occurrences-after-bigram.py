class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        list1 = text.split()
        res = []
        for i in range(len(list1) - 2):
            if list1[i] == first and list1[i+1] == second:
                res.append(list1[i+2])
        return res        

        