class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i = 0;
        int j = 1;
        int count = 1;
        while(j < nums.size()){
            if(nums[i] == nums[j]){
                
                count++;
                if(count > 2){
                    nums.erase(nums.begin()+j);
                    continue;
                }
                j++;
            }else{
                i = j;
                j++;
                count = 1;
            }
        }
        return  nums.size();
    }
};