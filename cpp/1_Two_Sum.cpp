class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> result;
        for(int i = 0;i<nums.size();i++){
            int compliment = target - nums[i];
            if(result.find(compliment) != result.end() ){
                return {result[compliment],i};
            }
            result[nums[i]] = i;
        }
        return {};
    }
};