class Solution {
public:
    double myPow(double x, int n) {
        long num = abs(n);
        double result = 1.0;
        while(num != 0){
            if(num %2 == 1){
                result*=x;
                num--;
            }
            x*=x;
            num/=2;
        }
        return n<0? 1.0/result : result;
    }
};