class NumArray {
    vector<int>s;
public:
    NumArray(vector<int>& nums) {
        int total{};
        for(int n:nums){
            total+=n;
            s.push_back(total);
        }
    }
    
    int sumRange(int left, int right) {
        int sright = s[right];
        int sleft = left>0?s[left-1]:0;
        return sright - sleft;
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */