# 🎯 LeetCode 1: Two Sum

![LeetCode](https://img.shields.io/badge/LeetCode-1-blue?style-for-the-badge&logo=leetcode)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style-for-the-badge)
![Topics](https://img.shields.io/badge/Topics-Array%2C%20Hash%20Table-brightgreen?style-for-the-badge)

---

## 📘 Problem Statement

> Given an array of integers `nums` and an integer `target`, return **indices of the two numbers** such that they add up to `target`.
>
> You may assume that each input would have **exactly one solution**, and you may not use the same element twice.
>
> You can return the answer in any order.

---

## 📥 Example Inputs

### ✅ Example 1:
```cpp
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
✅ Example 2:
C++

Input: nums = [3,2,4], target = 6
Output: [1,2]
✅ Example 3:
C++

Input: nums = [3,3], target = 6
Output: [0,1]
📌 Constraints
2 <= nums.length <= 10^4

-10^9 <= nums[i] <= 10^9

-10^9 <= target <= 10^9

Only one valid answer exists.

💡 Pattern & Approach
The problem asks us to find a pair of numbers that sum to a target. The most straightforward solution is to check every possible pair, but a more optimal solution uses a hash map for faster lookups.

Brute-Force Approach (Nested Loops)

One-Pass Hash Map (Optimal)

🔍 The Logic
🔹 Approach 1: Brute-Force Approach
The simplest way is to check every possible pair of numbers in the array to see if they sum up to the target.

Outer Loop

Iterate through the array with an index i from 0 to n-1.

Inner Loop

For each i, iterate through the rest of the array with an index j starting from i + 1 to avoid using the same element twice.

Check Sum

If nums[i] + nums[j] == target, we've found the solution. Return the indices {i, j}.

🔹 Approach 2: One-Pass Hash Map
To improve upon the O(N^2) time of the brute-force method, we can use a hash map to achieve O(1) average time complexity for lookups. As we iterate through the array, we check if the complement of the current number (i.e., target - current_number) has been seen before.

Initialize

Create a hash map to store numbers we've seen and their corresponding indices: map<number, index>.

Iterate and Check

Loop through the nums array with index i.

Calculate Complement

For each number nums[i], calculate its complement: complement = target - nums[i].

Find in Map

Check if the complement exists as a key in the hash map.

If it exists, we have found our pair. Return the index stored in the map (map[complement]) and the current index i.

Store in Map

If the complement is not found, add the current number nums[i] and its index i to the map for future checks.

🏃‍♂️ Dry Run Example (One-Pass Hash Map)
Given:
nums = [2,7,11,15], target = 9

i	nums[i]	Complement (9 - nums[i])	Map contains Complement?	Action	Map State
0	2	7	No	Add 2:0 to map	{2: 0}
1	7	2	Yes (map[2] exists)	Return {map[2], i} -> {0, 1}	{2: 0}
✅ Conclusion: The loop finds the complement 2 in the map at index 1 and immediately returns the answer [0, 1].

💻 C++ Code
Approach 1: Brute-Force

C++

#include <vector>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[i] + nums[j] == target) {
                    return {i, j};
                }
            }
        }
        return {}; // Should not be reached based on problem constraints
    }
};
Approach 2: One-Pass Hash Map

C++

#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        // Map to store: {number -> index}
        std::unordered_map<int, int> num_map;
        
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            
            // Check if the complement exists in the map
            if (num_map.count(complement)) {
                // If found, return the indices
                return {num_map[complement], i};
            }
            
            // If not found, add the current number and its index to the map
            num_map[nums[i]] = i;
        }
        
        return {}; // Should not be reached based on problem constraints
    }
};
📈 Time & Space Complexity
Approach           Time Complexity   Space Complexity
Brute-Force        O(N^2)            O(1)
One-Pass Hash Map  O(N)              O(N)
N: Number of elements in the nums array.

Time Complexity: The hash map approach is significantly faster as it only requires one pass through the array.

Space Complexity: The hash map approach uses extra space to store up to N elements.

🏷️ Tags
#Array #HashTable #LeetCode-Easy