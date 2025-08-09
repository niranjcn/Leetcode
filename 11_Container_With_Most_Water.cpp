class Solution {
public:
    int maxArea(vector<int>& height) {
        int i = 0;
        int j = height.size()-1;
        int maxcap = INT_MIN;
        
        while(i <j){
            int temp = (j-i) * min(height[i],height[j]);
            maxcap = max(temp,maxcap);
            if(height[i] < height[j]){
                i++;
            }else{
                j--;
            }
        }
        return maxcap;
    }
};