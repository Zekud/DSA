class Solution {
public:
    int reverse(int x) {
        int min = INT_MIN;
        int max = INT_MAX;
        int reversed = 0;
        while(x!=0){
            int last = x%10;
            if(reversed > (max/10)) return 0;
            if(reversed < (min/10)) return 0;
            reversed = reversed * 10 + last;
            x/=10;
        }
        return reversed;
    }
};