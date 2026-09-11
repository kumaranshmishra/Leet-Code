class Solution {
public:
    int countSetbit(int x){
        int count = 0;
        while(x>0){
            x = x & (x-1);
            count++;
        }
        return count;
    }
    vector<int> countBits(int n) {
        vector<int> res(n+1);
        for(int i = 0 ; i<=n;i++){
            res[i] = countSetbit(i);
        }
        return res;
    }
};