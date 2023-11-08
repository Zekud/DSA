class Solution {
public:
    bool isPalindrome(int x) {
        string pal = to_string(x);
        int left{0};
        int right = pal.length()-1;
        while(left<right){
            if(pal[left] != pal[right]){
                return false;
            }
            left++;
            right--;    
        }
        return true;
    }
};