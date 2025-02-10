class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def strsort(x,y):
            if int(str(x) + str(y)) > int(str(y) + str(x)):
                return -1  
            elif int(str(x) + str(y)) < int(str(y) + str(x)):
                return 1   
            else:
                return 0   
        nums_sorted = list(map(str, sorted(nums, key=cmp_to_key(strsort))))
        return str(int("".join(nums_sorted)))
