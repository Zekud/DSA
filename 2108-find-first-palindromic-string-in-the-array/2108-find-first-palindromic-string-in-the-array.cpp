class Solution {
public:
    string firstPalindrome(vector<string>& words) {
        for(auto s : words){
            int l=0,r=s.size()-1;
            bool check = false;
            while(l<r){
                if(s[l]!=s[r]){
                    check=true;
                    break;
                }
                l++;r--;
            }
            if(check)
                continue;
            else
                return s;    
        }
        return "";
    }
};