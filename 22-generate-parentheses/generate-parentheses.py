class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res=[]
        def backtrack(Open,Close,path):
            if Open==Close==n:
                res.append("".join(path))
                return
            if Open<n:
                path.append("(")
                backtrack(Open+1,Close,path)
                path.pop()
            if Close<Open:
                path.append(")")
                backtrack(Open,Close+1,path)
                path.pop()

        backtrack(0,0,[])
        return res