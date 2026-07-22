class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int right = 0;
        int left = 0;
        int n = s.length();
        int maxlen = 0;
        unordered_set<char> window;

        while(right < n){
            if(window.find(s[right]) == window.end()){
                window.insert(s[right]);
                maxlen = max(maxlen,right - left + 1);
                right++;
                
            }else{
                window.erase(s[left]);
                left++;
            }
        }
        return maxlen;
    }
};