class Solution {
public:
    vector<string> commonChars(vector<string>& words) {

        int arr[100][26] = {0};  

        for (int i = 0; i < words.size(); i++) {
            for (int j = 0; j < words[i].length(); j++) {
                char ch = words[i][j];
                arr[i][ch - 'a']++;
            }
        }

        vector<string> res;

        for (int i = 0; i < 26; i++) {
            int mn = arr[0][i];

            for (int j = 1; j < words.size(); j++) {
                if (arr[j][i] < mn) {
                    mn = arr[j][i];
                }
            }

            for (int k = 0; k < mn; k++) {
                res.push_back(string(1, char(i + 'a')));
            }
        }

        return res;
    }
};