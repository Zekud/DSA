class Solution:
    def removeStars(self, s: str) -> str:
        if len(s) == 0 or s=='*':
            return ''
        stack = []
        for char in s:
            if(char == '*'):
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)