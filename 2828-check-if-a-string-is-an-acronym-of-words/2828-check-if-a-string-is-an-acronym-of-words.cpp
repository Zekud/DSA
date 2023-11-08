class Solution {
public:
    bool isAcronym(vector<string>& words, string s) {
        string curr;
        for(auto word:words){
            curr+=word[0];
        }
        if(curr==s)
            return true;
        else 
            return false;
        
    }
};