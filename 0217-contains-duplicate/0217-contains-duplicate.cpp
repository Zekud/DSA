class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int>box;
        for(auto n:nums)
            box.insert(n);
        if(nums.size()>box.size())
            return true;
        else
            return false;
    }
};