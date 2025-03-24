class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        if len(s)<2:
            return
        stack=[]
        ans=0
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(s[i])
            else:
                temp = 0
                while  stack[-1] !="(":
                    temp += 2 * stack.pop()
                
                stack.pop()
                if temp != 0:
                    stack.append(temp)
                else:
                    stack.append(1)

                
        return sum(stack)