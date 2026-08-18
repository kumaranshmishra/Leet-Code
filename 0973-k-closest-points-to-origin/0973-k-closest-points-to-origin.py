import heapq as h
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        for x,y in points:
            d = x*x + y*y
            h.heappush(heap,(d,x,y))
        ans = []
        for i in range (k):
            d,x,y = h.heappop(heap)
            ans.append([x,y])
        return ans    



