class Solution {
public:
    vector<int> partitionLabels(string s) {
        vector<int> partitions;
        int start = 0;
        int end = 0;
        int lastOccurence[26];
        for(int i = 0; i<s.size();i++){
            char curr = s[i];
            lastOccurence[curr-'a'] = i;
        }
        for(int i = 0 ; i <s.size() ; i++){
            char curr = s[i];
            int lastIndex = lastOccurence[curr-'a'];
            end = max(end,lastIndex);
            if(i == end){
                partitions.push_back(end-start+1);
                start = i+1;
            }
        }
        return partitions;  
    }
};