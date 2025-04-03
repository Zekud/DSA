class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count_sorted = sorted(count.items(), key=lambda x: x[1],reverse=True)
        ans = []
        for key,val in count_sorted:
            ans.append(key)
            k-=1
            if k<1:
                break
            
        return ans

