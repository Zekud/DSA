class Solution
{
public:
    string mergeAlternately(string word1, string word2)
    {
        string merged = "";
        int n = word1.length();
        int m = word2.length();
        int l = word1.length() > word2.length() ? word1.length() : word2.length();

        for (int i = 0; i < l; ++i)
        {
            if (i < n)
                merged += word1[i];
            if (i < m)
                merged += word2[i];
        }
        return merged;
    }
};