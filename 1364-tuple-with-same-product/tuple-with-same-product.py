class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count = Counter()
        tuples = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if i != j:
                    count.update([nums[i] * nums[j]])

        for prod, value in count.items():
            pairs = value
            if pairs > 1:
                perm = math.perm(pairs, 2)
                tuples += perm * 4
        return tuples