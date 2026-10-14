class Solution {
public:
    vector<bool> canEat(vector<int>& candiesCount, vector<vector<int>>& queries) {
        vector<bool> ans;
        vector<long long> prefix_sum(candiesCount.size());

        prefix_sum[0] = candiesCount[0];

        for (int i = 1; i < candiesCount.size(); i++) {
            prefix_sum[i] = prefix_sum[i - 1] + candiesCount[i];
        }

        for (vector<int>& query : queries) {
            int favC = query[0];
            int favD = query[1];
            int dailyC = query[2];

            long long minCandies = favD + 1LL;
            long long maxCandies = (favD + 1LL) * dailyC;

            long long candiesBefore = (favC == 0) ? 0 : prefix_sum[favC - 1];
            long long candiesThrough = prefix_sum[favC];

            if (maxCandies > candiesBefore && minCandies <= candiesThrough) {
                ans.push_back(true);
            } else {
                ans.push_back(false);
            }
        }

        return ans;
    }
};