class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> maps;
        unordered_map<char, char> mapt;
        if (s.size()!=t.size()){
            return false ;
        }
        for (int i= 0; i<s.size();i++){
            char char_s = s[i];

            char char_t = t[i];
             if (maps.find(char_s) == maps.end()) {
                maps[char_s] = char_t;
            }
            if (mapt.find(char_t) == mapt.end()) {
                mapt[char_t] = char_s;
            }

            if (maps[char_s] != char_t || mapt[char_t] != char_s) {
                return false;
        }
        
    }
    return true;}
};