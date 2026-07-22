class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int j =0;
        for(int i =1;i<nums.size();){
            if(nums[i] == nums[j]){
                nums.erase(nums.begin()+j);
            }
            else{
                
                j++;
                i++;
            }
        }
        return nums.size();
    }
};