class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans =[]
        i,j=0,0
        while i<len(firstList) and j < len(secondList):

            maxi = max(firstList[i][0],secondList[j][0])
            mini  = min(firstList[i][1],secondList[j][1])
            if maxi<=mini:
                ans.append([maxi,mini])
            if firstList[i][1] < secondList[j][1]:
                i+=1
            elif firstList[i][1] >secondList[j][1]:
                j+=1
            else:
                i+=1
                j+=1
        return ans
            


        