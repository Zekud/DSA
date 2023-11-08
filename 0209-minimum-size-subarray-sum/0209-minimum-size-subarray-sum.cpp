class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int length = nums.size()+1;
        int total=0,l=0;
        
        for(int i=0;i<nums.size();++i){
            total+=nums[i];
            while(total>=target){
                length = min(length,i-l+1);
                total-=nums[l];
                l++;
            }
        }
        if(length == nums.size()+1)
            return 0;
        else
            return length;
    }
};