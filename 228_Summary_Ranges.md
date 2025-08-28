# 📈 LeetCode 228: Summary Ranges

![LeetCode](https://img.shields.io/badge/LeetCode-228-blue?style-for-the-badge&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style-for-the-badge)
![Topics](https://img.shields.io/badge/Topics-Array-brightgreen?style-for-the-badge)

---

## 📘 Problem Statement

> You are given a **sorted unique** integer array `nums`.
>
> A **range** `[a,b]` is the set of all integers from `a` to `b` (inclusive).
>
> Return the **smallest sorted** list of ranges that **cover all the numbers in the array exactly**. That is, each element of `nums` is covered by exactly one of the ranges, and there is no integer `x` such that `x` is in one of the ranges but not in `nums`.
>
> Each range `[a,b]` in the list should be output as:
> - `"a->b"` if `a != b`
> - `"a"` if `a == b`

---

## 📥 Example Inputs

### ✅ Example 1:
```cpp
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:

[0,2] --> "0->2"

[4,5] --> "4->5"

[7,7] --> "7"

✅ Example 2:
C++

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
📌 Constraints
0 <= nums.length <= 20

-2^31 <= nums[i] <= 2^31 - 1

All the values of nums are unique.

nums is sorted in ascending order.

💡 Pattern & Approach
Since the input array is sorted, we can solve this with a single pass. The pattern is to iterate through the array and identify consecutive sequences of numbers, building a range for each sequence as we go.

Iterative Range Building (Single Pass)

🔍 The Logic
🔹 Approach: Iterative Range Building
We use a single pointer to traverse the array, and an inner loop to find the end of each consecutive range.

Initialize

Create an empty result vector of strings.

Use a pointer i to iterate through nums, starting at 0.

Outer Loop

The main while loop continues as long as i is within the bounds of the array.

Identify Range Start

At the beginning of each iteration, the number nums[i] is the start of a potential new range. Store it in a start variable.

Find Range End

Use an inner while loop to look ahead.

As long as the next element nums[i+1] is exactly one greater than the current element nums[i], we are in a consecutive sequence. Keep incrementing i to extend the current range.

Format and Add to Result

The inner loop stops when the sequence is broken or the array ends. At this point, nums[i] is the end of the range.

Compare start and end:

If they are the same, format the string as "start".

If they are different, format it as "start->end".

Push the formatted string into the result vector.

Advance to Next Range

Increment i one more time to move past the end of the completed range and begin searching for the next one.

🏃‍♂️ Dry Run Example
Given:
nums = [0,1,2,4,5,7]

Outer Loop i	start	Inner Loop Condition (nums[i+1] == nums[i]+1)	i after inner loop	end	Result Added	result state
0	0	1==0+1 (True), 2==1+1 (True), 4!=2+1 (False)	2	2	"0->2"	["0->2"]
3	4	5==4+1 (True), 7!=5+1 (False)	4	5	"4->5"	["0->2", "4->5"]
5	7	(end of array)	5	7	"7"	["0->2", "4->5", "7"]

Export to Sheets
✅ Conclusion: The loop finishes. Final result is ["0->2","4->5","7"].

💻 C++ Code
C++

#include <vector>
#include <string>

class Solution {
public:
    std::vector<std::string> summaryRanges(std::vector<int>& nums) {
        int n = nums.size();
        std::vector<std::string> result;
        int i = 0;

        while (i < n) {
            // Mark the start of a new range.
            int start = nums[i];

            // Look ahead to find the end of the consecutive sequence.
            while (i + 1 < n && nums[i + 1] == nums[i] + 1) {
                i++;
            }
            
            // Mark the end of the range.
            int end = nums[i];

            // Format the string based on whether it's a single number or a range.
            if (start == end) {
                result.push_back(std::to_string(start));
            } else {
                result.push_back(std::to_string(start) + "->" + std::to_string(end));
            }
            
            // Move to the next potential start of a range.
            i++;
        }
        
        return result;
    }
};
📈 Time & Space Complexity
Approach              Time Complexity   Space Complexity
Iterative Range Building  O(N)              O(1)
N: Number of elements in the nums array.

Time Complexity: We traverse the array with a single pass. Although there is a nested loop, the pointer i only moves forward, ensuring each element is visited exactly once.

Space Complexity: O(1) extra space is used, not counting the space required for the result vector. The result vector's space depends on the number of ranges, which is at most O(N).

🏷️ Tags
#Array #Iteration #LeetCode-Easy