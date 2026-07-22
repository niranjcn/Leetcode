class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> sorted;
        vector<vector<string>> result;
        for(auto &str : strs){
            string key = str;
            sort(key.begin(),key.end());
            sorted[key].push_back(str);
        }

        for(auto &entry : sorted){
            result.push_back(entry.second);
        }
        return result;
    }
};