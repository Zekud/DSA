class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxque = deque()
        minque = deque()
        subbeg = 0
        leng = 0
        for i in range(len(nums)):
            while maxque and maxque[-1] < nums[i]:
                maxque.pop()
            maxque.append(nums[i])
            while minque and minque[-1] > nums[i]:
                minque.pop()
            minque.append(nums[i])

            while maxque[0]-minque[0]  > limit:
                if minque[0] == nums[subbeg]:
                    minque.popleft()
                if maxque[0] == nums[subbeg]:
                    maxque.popleft()
                subbeg+=1
            curlen = i - subbeg +1
            leng = max(leng , curlen)
        return leng
        

                