class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        target = len(arr)
        ans=[]
        while target>0:
            mx = arr.index(target)
            if mx == 0:
                arr[:target] = arr[:target][::-1]
                ans.append(target)
                target -= 1
            else:
                arr[:mx+1] = arr[:mx+1][::-1]
                arr[:target] = arr[:target][::-1]
                ans.append(mx+1)
                ans.append(target)
                target-=1
                       
        return ans