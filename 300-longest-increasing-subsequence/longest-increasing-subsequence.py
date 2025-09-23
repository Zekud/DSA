class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = [nums[0]]
        n = len(nums)
        for i in range(1,n):
            if arr[-1] < nums[i]:
                arr.append(nums[i])
            else:
                idx = bisect_left(arr,nums[i])
                arr[idx] = nums[i]
        return len(arr)
