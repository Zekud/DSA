class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        foccur = float("inf")
        loccur = float("-inf")

        def bsearch(target,start,end,occ): 
            nonlocal foccur,loccur
            while start <= end:
                mid = start + (end-start)//2
                if nums[mid] == target:
                    if occ == "first":
                        foccur = min(mid,foccur)
                        end= mid-1
                    else:
                        loccur = max(mid,loccur)
                        start = mid+1
                elif nums[mid] > target:
                    end = mid-1
                else:
                    start = mid+1
            if occ == "first" and foccur != float("inf"):
                return foccur
            elif occ == "last" and loccur != float("-inf"):
                return loccur
            else:
                return -1
        first = bsearch(target,0,len(nums)-1,"first")
        last = bsearch(target,0,len(nums)-1,"last")
        return [first,last]
        
        
