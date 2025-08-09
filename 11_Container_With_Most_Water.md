LeetCode Problem 11: Container With Most Water






📘 Problem Statement
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that, together with the x-axis, form a container such that the container contains the most water.

Return the maximum amount of water a container can store.

Note: You may not slant the container.

📥 Example Inputs
✅ Example 1:
Input:

cpp
Copy
Edit
height = [1,8,6,2,5,4,8,3,7]
Output:

cpp
Copy
Edit
49
Explanation:
The above vertical lines are represented by the array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water the container can contain is 49.

✅ Example 2:
Input:

cpp
Copy
Edit
height = [1,1]
Output:

cpp
Copy
Edit
1
📌 Constraints
n == height.length

2 <= n <= 10^5

0 <= height[i] <= 10^4

Pattern
Two-pointer technique

Greedy shrinking: Move the pointer from the shorter height inward to potentially find a taller line.

Approach
Start with two pointers:

i = 0 (leftmost line)

j = n-1 (rightmost line)

Calculate the area using:

(
𝑗
−
𝑖
)
×
min
⁡
(
ℎ
𝑒
𝑖
𝑔
ℎ
𝑡
[
𝑖
]
,
ℎ
𝑒
𝑖
𝑔
ℎ
𝑡
[
𝑗
]
)
(j−i)×min(height[i],height[j])
Update maxcap if this area is larger than the previous maximum.

Move the pointer pointing to the shorter line inward:

If height[i] < height[j], increment i

Else, decrement j

Continue until i meets j.

Dry Run
Example:

ini
Copy
Edit
height = [1,8,6,2,5,4,8,3,7]
i	j	height[i]	height[j]	width	min height	area	maxcap
0	8	1	7	8	1	8	8
1	8	8	7	7	7	49	49
1	7	8	3	6	3	18	49
1	6	8	8	5	8	40	49
1	5	8	4	4	4	16	49
1	4	8	5	3	5	15	49
1	3	8	2	2	2	4	49
1	2	8	6	1	6	6	49

Result: 49

This works in O(n) time because each pointer only moves inward once.

💻 C++ Code
cpp
Copy
Edit
class Solution {
public:
    int maxArea(vector<int>& height) {
        int i = 0;
        int j = height.size() - 1;
        int maxcap = INT_MIN;

        while (i < j) {
            int temp = (j - i) * min(height[i], height[j]);
            maxcap = max(temp, maxcap);
            if (height[i] < height[j]) {
                i++;
            } else {
                j--;
            }
        }
        return maxcap;
    }
};
📈 Time & Space Complexity
Complexity	Value
Time	O(n)
Space	O(1) — constant

🏷 Tags
#TwoPointers #Greedy #Array #LeetCode-Medium #Math