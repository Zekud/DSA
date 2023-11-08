class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
       vector<int>result;
        int leftp = 1;
        int rightp = 1;
        for(int i=0;i<nums.size();++i){
            result.push_back(leftp);
            leftp*=nums[i];
        }
        for(int i=nums.size()-1;i>=0;--i){
            int r = rightp * result[i];
            result[i] = r;
            rightp*=nums[i];
        }
        return result;
    }
};