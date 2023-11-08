class Solution {
public:
    int trailingZeroes(int n) {
        int count = 0;
        int multipleOfFive = 5;
        while(n>=multipleOfFive){
            count += (n/multipleOfFive);
            multipleOfFive *= 5;
        }
        return count;
    }
};