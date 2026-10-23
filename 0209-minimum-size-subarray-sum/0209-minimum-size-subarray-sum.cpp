class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
    int start = 0;
    int m = INT_MAX;
    int window_sum = 0;
    for(int i = 0 ; i<nums.size();i++){
        window_sum += nums[i];
        while(window_sum>=target){
            m = min(m,i - start +1);
            window_sum -= nums[start];
            start++; 
        } 
    }
    if(m == INT_MAX)return 0;
else return m;
    }
};