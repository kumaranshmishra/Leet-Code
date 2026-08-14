class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = {}
        for i in range(len(list1)):
            if list1[i] in list2:
                j= list2.index(list1[i])
                if i+j not in res:
                    res[i+j] = []
                res[i+j].append(list1[i])
        min_sum = min(res.keys())
        return res[min_sum]
        