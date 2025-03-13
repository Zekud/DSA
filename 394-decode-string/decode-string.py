class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num_stack = []
        arr = []
        res = ""
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = ""
                while s[i].isdigit():
                    num += s[i]
                    i+=1
                num_stack.append(int(num))
                i-=1
            elif s[i] == "]":
                while stack and stack[-1] != "[":
                    arr.append(stack.pop())
                if stack and stack[-1] == "[":
                    stack.pop()
                if num_stack:
                    stack.append("".join(reversed(arr)) * num_stack.pop())
                else:
                    stack.append("".join(reversed(arr)))
                res = "".join(stack)
                arr = []
            else:
                stack.append(s[i])
            i+=1
        print(stack)
        print(res)
        return "".join(stack)