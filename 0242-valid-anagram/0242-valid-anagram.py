class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_counter = {}
        for char in s:
            char_counter[char] = char_counter.get(char,0) + 1
        for char in t:
            if char not in char_counter or char_counter[char] == 0:
                return False
            char_counter[char]-=1
        return all(char == 0 for char in char_counter.values())
        