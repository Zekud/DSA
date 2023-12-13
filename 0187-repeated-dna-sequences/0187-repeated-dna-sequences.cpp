class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        map<string,int>sequence;
        vector<string> result;
        if(s.length()<10) return result;
        
        for(int i=0;i<=s.length()-10;++i){
            sequence[s.substr(i,10)]++;
        }
        for(auto seq : sequence){
            if(seq.second > 1)
                result.push_back(seq.first);
        }
        return result;
        
        
    }
};