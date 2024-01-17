class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        nums_count = {}
        for num in arr:
            nums_count[num] = nums_count.get(num,0) + 1
        return len(set(nums_count.values())) == len(nums_count.values())