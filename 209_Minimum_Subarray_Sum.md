📏 LeetCode 209: Minimum Size Subarray Sum
📘 Problem Statement
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

📥 Example Inputs
✅ Example 1:
Input:

C++

target = 7, nums = [2,3,1,2,4,3]
Output:

C++

2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

✅ Example 2:
Input:

C++

target = 4, nums = [1,4,4]
Output:

C++

1
✅ Example 3:
Input:

C++

target = 11, nums = [1,1,1,1,1,1,1,1]
Output:

C++

0
📌 Constraints
1 <= target <= 10^9

1 <= nums.length <= 10^5

1 <= nums[i] <= 10^4

💡 Pattern & Approach (O(n) Solution)
The most efficient way to solve this problem is using the Sliding Window technique. This pattern is ideal for finding a minimum or maximum length subarray that satisfies a certain condition.

The Logic
We'll maintain a "window" over the array, represented by a left and right pointer. We expand this window by moving the right pointer and shrink it by moving the left pointer.

Initialization:

A left pointer starting at index 0.

A sum to track the sum of elements inside the current window, initialized to 0.

A minLen variable to store the minimal length found so far, initialized to a very large value (e.g., INT_MAX).

Expand the Window: Iterate through the array with a right pointer from 0 to the end. In each step, add nums[right] to the sum. This makes the window wider.

Check and Shrink the Window: After expanding, check if the sum is greater than or equal to the target.

If it is, we have a valid subarray!

First, we update minLen with the current window's length (right - left + 1) if it's smaller.

Then, to find an even smaller valid window, we must shrink the window from the left. We do this by subtracting nums[left] from the sum and incrementing left.

We repeat this shrinking process within a while loop until the sum is no longer >= target.

Final Result: After the right pointer has traversed the entire array, if minLen is still INT_MAX, it means no valid subarray was ever found, so we return 0. Otherwise, we return the stored minLen.

🏃‍♂️ Dry Run
Let's trace the sliding window for target = 7, nums = [2,3,1,2,4,3].
Initial state: left = 0, sum = 0, minLen = ∞

right	nums[right]	sum	sum >= 7?	Action	Window Len	minLen	left
0	2	2	No	Expand	-	∞	0
1	3	5	No	Expand	-	∞	0
2	1	6	No	Expand	-	∞	0
3	2	8	Yes	1. Update minLen<br/>2. Shrink (sum -= nums[0])	4	4	1
6	No	while loop ends	-	4	1
4	4	10	Yes	1. Update minLen<br/>2. Shrink (sum -= nums[1])	4	4	2
7	Yes	1. Update minLen<br/>2. Shrink (sum -= nums[2])	3	3	3
6	No	while loop ends	-	3	3
5	3	9	Yes	1. Update minLen<br/>2. Shrink (sum -= nums[3])	3	3	4
7	Yes	1. Update minLen<br/>2. Shrink (sum -= nums[4])	2	2	5
3	No	while loop ends	-	2	5
The loop finishes. The final answer is minLen = 2.

💻 C++ Code (O(n) Solution)
C++

#include <vector>
#include <algorithm> // For std::min
#include <climits>   // For INT_MAX

class Solution {
public:
    int minSubArrayLen(int target, std::vector<int>& nums) {
        int left = 0;
        long long sum = 0; // Use long long for sum to avoid overflow, though not strictly needed with given constraints
        int minLen = INT_MAX;
        
        // 1. Iterate through the array with the right pointer to expand the window
        for (int right = 0; right < nums.size(); right++) {
            sum += nums[right];
            
            // 2. When the sum is valid, shrink the window from the left
            while (sum >= target) {
                // Update the minimum length found so far
                minLen = std::min(minLen, right - left + 1);
                
                // Shrink the window
                sum -= nums[left];
                left++;
            }
        }
        
        // 3. If minLen was never updated, no valid subarray was found
        return (minLen == INT_MAX) ? 0 : minLen;
    }
};
📈 Time & Space Complexity
Complexity	Value	Justification
Time	O(n)	Although there is a nested while loop, each element is visited at most twice: once by the right pointer and once by the left pointer. This results in a linear time complexity.
Space	O(1)	We only use a constant amount of extra space for the left pointer, sum, and minLen variables, regardless of the input size.
Follow-up: O(n
logn) Solution
The problem asks for an O(n
logn) solution. This can be achieved with Prefix Sums and Binary Search.

Create Prefix Sums: First, calculate a prefix sum array, let's call it prefix, of size n+1. prefix[i] will store the sum of the first i elements of nums.

Iterate and Search: Iterate through the prefix array from i = 1 to n. For each prefix[i], we need to find the smallest subarray ending at i-1 that sums to at least target. This means we are looking for the earliest starting index j such that sum(nums[j]..nums[i-1]) >= target.

The Condition: Using prefix sums, this condition is prefix[i] - prefix[j] >= target. Rearranging this, we get prefix[j] <= prefix[i] - target.

Binary Search: To find the largest j (which corresponds to the smallest subarray length i-j) that satisfies this, we can use binary search (specifically, a function like upper_bound) on the prefix array for the value prefix[i] - target. This search takes O(
logn) time.

Since we do this search for each of the n elements, the total time complexity is O(n
logn).

🏷️ Tags
#SlidingWindow #TwoPointers #Array #BinarySearch #LeetCode-Medium