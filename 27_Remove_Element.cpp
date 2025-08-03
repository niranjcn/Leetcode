class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int i = 0;
        int j = 0;
        for(i = 0; i < nums.size(); i++){
            if(nums[i] == val){
                continue;
            }else if(nums[j] == val){
                swap(nums[i],nums[j]);
                j++;
            }else{
                j++;
            }
             
        }
        return j;
    }
};