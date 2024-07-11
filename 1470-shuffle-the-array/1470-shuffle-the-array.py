class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if len(nums) <= 2:
            return nums
        i,j = 0,n
        lst = []
        while i<n:
            lst.append(nums[i])
            lst.append(nums[j])
            i+=1
            j+=1
        return lst