class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length()) return false;
        unordered_map<char,int> s_count;
        

        for(char c : s){
            s_count[c]++;
        }
        for(char c : t){
            s_count[c]--;
            if(s_count[c] < 0) return false;
        }

        
        return true;
    }

};