class Solution:
    def isValid(self, s: str) -> bool:
        chars = {')':'(',']':'[','}':'{'}
        stack = []
        for char in s:
            if char in chars:
                if len(stack)!=0 and stack[-1] == chars[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack)==0
        
        