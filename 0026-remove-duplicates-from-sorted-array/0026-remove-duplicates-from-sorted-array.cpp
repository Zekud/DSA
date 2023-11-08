class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
      
        int l=0,j=1;
        while(j<nums.size()){
            if(nums[j]!=nums[l]){
                l++;
                nums[l]=nums[j];
            }
            j++;
        }
        return l+1;
    }
};