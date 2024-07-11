class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if len(nums) <= 2:
            return nums
        k=0
        fst = nums[0:n]
        scd = nums[n:]
        for i in fst:
            nums[k] = i
            k+=2
        k=1
        for i in scd:
            nums[k] = i
            k+=2
        return nums