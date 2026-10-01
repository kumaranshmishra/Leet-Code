class Solution {
public:
    bool isValid(string s) {
        stack<char>res;
        for(int i = 0 ; i <s.size();i++){
            if (res.size() == 0){
                res.push(s[i]);
            }
           else if (res.top()=='(' && s[i] == ')' || res.top()=='{' && s[i] == '}'||res.top()=='[' && s[i] == ']' ){
                res.pop();
            }
            else{
                res.push(s[i]);
            }
        }
        if (res.size() == 0 ) return true;
        else return false;
        
    }
};