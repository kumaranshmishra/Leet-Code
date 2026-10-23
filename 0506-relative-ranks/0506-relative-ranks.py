class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        sorted_score = sorted(score,reverse = True)
        res = []
        for i in score:
            x = sorted_score.index(i)
            if x == 0:
                res.append("Gold Medal")   
            elif x == 1:
                res.append("Silver Medal")
            elif x == 2:
                res.append("Bronze Medal")
            else:
                res.append(str(x+1))
        return res                      