class Solution {
public:
    vector<string> commonChars(vector<string>& words) {

       vector<string> res;
       for (char c : words[0]) {
           if (all_of(words.begin(), words.end(), [c](const string& word) { return word.find(c) != string::npos; })) {
               res.push_back(string(1, c));
               for (int j = 1; j < words.size(); ++j) {
                   size_t pos = words[j].find(c);
                   if (pos != string::npos) {
                       words[j].erase(pos, 1);
                   }
               }
           }
       }
         return res; 
        
    }
};