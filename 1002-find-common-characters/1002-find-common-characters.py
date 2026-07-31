class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        for i in words[0]:
            if all(i in word for word in words):
                res.append(i)
                for j in range(1, len(words)):
                    words[j] = words[j].replace(i, "", 1)
        return res