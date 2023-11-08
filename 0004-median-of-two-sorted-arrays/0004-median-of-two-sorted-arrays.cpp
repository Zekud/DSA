class Solution
{
public:
    double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2)
    {
        copy(nums2.begin(), nums2.end(), back_inserter(nums1));
        sort(nums1.begin(), nums1.end());
        int total = nums1.size();
        if (total % 2 == 0)
        {
            return ((nums1[(total / 2 - 1)] + nums1[(total / 2)]) / 2.0);
        }
        else
        {
            return (nums1[(total + 1) / 2 - 1]);
        }
    }
};