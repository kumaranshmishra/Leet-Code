class Solution {
public:
    int characterReplacement(string s, int k) {
    int start = 0;
    int res = 0;
    int max_freq = 0;
    unordered_map<char,int> frequency_map ;
    for(int end = 0 ; end < s.size();end++){
        frequency_map[s[end]]++;
        max_freq = max(frequency_map[s[end]], max_freq);
        while(end - start + 1 - max_freq > k){
            frequency_map[s[start]]--;
            start++;

        }
        res = max(res,end-start+1);


    }
    return res;




    }


};