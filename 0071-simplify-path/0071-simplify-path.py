class Solution:
    def simplifyPath(self, path: str) -> str:
        folders = [folder for folder in path.split('/') if folder]
        stack = []
        for folder in folders:
            if folder == ".." and stack:
                stack.pop()
            else:
                if folder not in ['.','..']:
                    stack.append(folder)
        return '/' + '/'.join(stack)
        