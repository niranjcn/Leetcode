class Solution {
public:
    bool wordPattern(string pattern, string s) {
        vector<string> words;
        string word;
        unordered_map<char,string> pat;
        unordered_map<string,char> s_to_p;
        stringstream ss(s);
        while(ss >> word){
            words.push_back(word);
        }
        if(pattern.length() != words.size()) return false;
        for(int i = 0;i < pattern.length();i++){
            char sp = pattern[i];
            string wor = words[i];
            if(pat.count(sp) && pat[sp] != wor) return false;
            if(s_to_p.count(wor) && s_to_p[wor] != sp) return false;

            pat[sp] = wor;
            s_to_p[wor] = sp;
        }
        return true;
    }
};