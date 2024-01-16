class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        chars_count = dict()
        for char in ransomNote:
            chars_count[char] = chars_count.get(char,0) + 1
        for char in magazine:
            if char in chars_count and chars_count[char]>0 :
                chars_count[char]-=1
        return all(count==0 for count in chars_count.values())