class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
class Solution:
    def __init__(self):
        self.root = TrieNode()

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        for word in words:
            curr = self.root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                curr.count += 1

        ans = []
        for word in words:
            sm = 0
            curr = self.root
            for c in word:
                if c in curr.children:
                    curr = curr.children[c]
                    sm += curr.count
            ans.append(sm)
        return ans
            