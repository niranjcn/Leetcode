class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        
        int n = nums.size();
        
        
        sort(nums.begin(),nums.end());
        for(int i=0; i<nums.size()-2;i++){
            int j = i+1;
            int k = n-1;
            while(j < k){
                int sum = nums[i] + nums[j] + nums[k];
                if(sum == 0){
                    result.push_back({nums[i] , nums[j] , nums[k]});
                    j++;
                    k--;
                    while(j < k && nums[j] == nums[j-1]){
                        j++;
                    }
                    while(j < k && nums[k] == nums[k+1]){
                        k--;
                    }
                }else if(sum > 0){
                    k--;
                }else{
                    j++;
                }
            }
            while(i < n - 1  && nums[i] == nums[i+1]){
                i++;
            }
            
        }
        return result;
    }
};