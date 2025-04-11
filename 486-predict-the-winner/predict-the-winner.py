class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def check(left,right):
            if left == right:
                return nums[left]
            
            left_choice = nums[left] - check(left+1,right)
            right_choice= nums[right] - check(left, right-1)

            return max(left_choice, right_choice)
        return check(0, len(nums)-1) >=0