class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        ans = []
        while i < len(nums):
            if nums[i] == i+1:
                i+=1
            else:
                if nums[i] == nums[nums[i]-1]:
                    if nums[i] not in ans:
                        ans.extend([nums[i]])
                    i+=1
                else:
                    nums[nums[i]-1],nums[i] = nums[i], nums[nums[i]-1]

        for i in range(len(nums)):
            if i != nums[i]-1:
                ans.append(i+1)
                break
        return ans
            