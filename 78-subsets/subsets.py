class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        for i in range(1<<n):
            bit = format(i,f"0{n}b")
            print(bit)
            temp = []
            for j,num in enumerate(bit):
                if num == "1":
                    temp.append(nums[j])
            ans.append(temp)
        return ans