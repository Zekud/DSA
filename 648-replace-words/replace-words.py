class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class Solution:
    def __init__(self):
        self.root = TrieNode()

    def replaceWords(self, dictionary: List[str], sentence: str) -> str: 
        for word in dictionary:
            curr = self.root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.is_end = True

        arr = sentence.split()
        ans = []
        for word in arr:
            replace = []
            curr = self.root
            flag = False
            for char in word:
                if char not in curr.children:
                    flag = True
                    break
                curr = curr.children[char]
                replace.append(char)
                if curr.is_end:
                    break
            if flag:
                ans.append(word)
            else:
                ans.append("".join(replace))
        return " ".join(ans)
            
            



