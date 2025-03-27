class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def validate(mid):
            num_sweep = [0]*(len(nums)+2)
            for i in range(mid+1):
                l,r,v = queries[i]
                num_sweep[l]+=v
                num_sweep[r+1] -=v
            for i in range(1,len(num_sweep)):
                num_sweep[i]+=num_sweep[i-1]
            flag = True
            for i in range(len(nums)):
                if num_sweep[i] < nums[i]:
                    flag = False
                    break
            return flag
        if sum(nums)==0:
            return 0
        ans=-1
        low , high = 0,len(queries) -1
        while low<=high:
            mid = (low + high)//2
            if validate(mid):
                ans = mid+1
                high= mid-1
            else:
                low = mid +1
        return ans
