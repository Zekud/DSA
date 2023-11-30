class Solution {
public:
    string reverseVowels(string s) {
        set<char> vowels = {'a','e','i','o','u','A','E','I','O','U'};
        int start = 0;
        int end = s.length()-1;
        while(start<end){
            while(start<end && !vowels.contains(s[start]))
                start++;
            while(end > start && !vowels.contains(s[end]))
                end--;
            char temp = s[start];
            s[start] = s[end];
            s[end] = temp;
            start++;
            end--;
        }
        return s;
    }
};