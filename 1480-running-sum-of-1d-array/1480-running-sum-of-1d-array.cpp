class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        int n = size(nums);
        int s  = nums[0];
        for(int i = 1 ; i<n;i++){
            nums[i] = nums[i] + s;
            s = nums[i];
        }
return nums;
        
    }
};