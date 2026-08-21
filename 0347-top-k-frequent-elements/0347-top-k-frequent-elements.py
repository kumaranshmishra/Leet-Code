class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}

        for i in range(len(nums)):
            res[nums[i]] = res.get(nums[i], 0) + 1

        ans = []

        for _ in range(k):
            max_count = 0
            max_key = None

            for key, value in res.items():
                if value > max_count:
                    max_count = value
                    max_key = key

            ans.append(max_key)
            del res[max_key]

        return ans
        