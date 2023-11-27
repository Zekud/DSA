class Solution {
public:
    bool isPerfectSquare(int num) {
        if(num==0 || num==1)
            return true;
        int start = 1;
        int end = num;
        while(start <= end){
            double mid = start + (end-start)/2;
            if(mid*mid >  num)
                end = mid - 1.0;
            else if(mid*mid ==  num)
                return true;
            else
                start = mid + 1.0;
        }
        return false;
    }
};