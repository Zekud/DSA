class Solution {
public:
    bool isPalindrome(string s) {
        string s2;
        for(char c:s){
            if(isalnum(c))
                s2+=tolower(c);
        }
        int l=0,r=s2.length()-1;
        while(l<r){
            if(s2[l]!=s2[r])
                return false;
            l++;
            r--;
        }
        return true;
    }
};