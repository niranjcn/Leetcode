# 🧼 LeetCode Problem: Remove Duplicates from Sorted Array (Problem #26)

![LeetCode](https://img.shields.io/badge/LeetCode-Remove%20Duplicates%20from%20Sorted%20Array-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-success)
![Language](https://img.shields.io/badge/Language-C%2B%2B-blue)
![Time Complexity](https://img.shields.io/badge/Time%20Complexity-O(n)-brightgreen)
![Space Complexity](https://img.shields.io/badge/Space%20Complexity-O(1)-blueviolet)

---

## 📘 Problem Statement

> Given a **sorted** integer array `nums`, remove the **duplicates in-place** such that each unique element appears only **once** and return the number of unique elements.
>
> The relative order of the elements should be preserved.
>
> The output should be stored in the first `k` indices of `nums`. The remaining elements beyond `k` don't matter.

---

## 🧪 Custom Judge Will Check

```cpp
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
📥 Example Inputs
✅ Example 1:
makefile
Copy
Edit
Input: nums = [1,1,2]  
Output: 2  
Updated nums = [1,2,_]
✅ Example 2:
makefile
Copy
Edit
Input: nums = [0,0,1,1,1,2,2,3,3,4]  
Output: 5  
Updated nums = [0,1,2,3,4,_,_,_,_,_]
📌 Constraints
1 <= nums.length <= 30,000

-100 <= nums[i] <= 100

nums is sorted in non-decreasing order

🧠 Algorithm Explanation — Two Pointer with erase()
🔧 Logic:
Use two pointers:

j — keeps track of the last unique value

i — scans the array

If nums[i] == nums[j], that means it's a duplicate — remove it using erase().

If it’s a new unique value, increment both i and j.

Since erase() shifts elements, i is only incremented when no deletion happens.

📷 Visual Representation

Image Credit: LeetCode

💡 C++ Code
```
    class Solution {
    public:
        int removeDuplicates(vector<int>& nums) {
            int j = 0;
            for(int i = 1; i < nums.size();){
                if(nums[i] == nums[j]){
                    nums.erase(nums.begin() + j);  // Remove the duplicate
                } else {
                    j++;
                    i++;
                }
            }
            return nums.size();  // The length of array after removing duplicates
        }
    };

```
```
    📈 Time & Space Complexity
    Complexity	Value
    Time	O(n²) (because of erase() inside the loop)
    Space	O(1) (in-place)
```

🔁 Note: A more optimal solution would avoid erase() and use index swapping instead to achieve O(n).

🏷 Tags
#Arrays #TwoPointers #InPlaceAlgorithm #LeetCode-Easy

🔗 Useful Resources
📘 Official Problem on LeetCode

📊 Editorial with Optimal Solution
