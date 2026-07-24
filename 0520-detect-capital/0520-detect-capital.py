class Solution(object):
    def detectCapitalUse(self, word):
        upper = 0

        for i in range(len(word)):
            if ord(word[i]) >= 65 and ord(word[i]) <= 90:
                upper += 1

        if upper == len(word):
            return True

        if upper == 0:
            return True

        if upper == 1 and ord(word[0]) >= 65 and ord(word[0]) <= 90:
            return True

        return False