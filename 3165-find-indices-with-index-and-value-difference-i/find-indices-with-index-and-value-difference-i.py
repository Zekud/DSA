class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if abs(i-j) >= indexDifference and abs(nums[i]-nums[j]) >=valueDifference:
                    ans.append(i)
                    ans.append(j)
                    break
        return ans if ans else [-1,-1]