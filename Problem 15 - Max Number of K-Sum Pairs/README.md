# 1679. Max Number of K-Sum Pairs

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/max-number-of-k-sum-pairs/description/)

---

## Problem Description

You are given an integer array `nums` and an integer `k`.

In one operation, you can pick two numbers from the array whose sum equals `k` and remove them from the array.

Return the maximum number of operations you can perform on the array.

---

## Examples

**Example 1:**

```
Input: nums = [1,2,3,4], k = 5  
Output: 2  
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
```

**Example 2:**

```
Input: nums = [3,1,3,4,3], k = 6  
Output: 1  
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
```

---

## Constraints

- `1 <= nums.length <= 10^5`  
- `1 <= nums[i] <= 10^9`  
- `1 <= k <= 10^9`

---

## Solution Strategy

To solve this problem, I used a **two-pointer** approach with sorting:

1. **Sort the array** to enable the two-pointer technique
2. **Initialize pointers**: `low = 0` (start) and `high = len(nums) - 1` (end)
3. **Initialize counter**: `count = 0` to track successful operations
4. **Loop while `low < high`**:
   - If `nums[low] + nums[high] == k`, we found a pair:
     - Increment `count`
     - Move both pointers inward (`low += 1`, `high -= 1`)
   - If sum is less than `k`, we need a larger sum → move `low += 1`
   - If sum is greater than `k`, we need a smaller sum → move `high -= 1`
5. **Return** the total count of operations.

### Why This Approach?

The two-pointer technique on a sorted array efficiently finds all valid pairs:
- **Time Complexity:** O(n log n) - Dominated by the sorting step
- **Space Complexity:** O(1) - Only using pointer variables (excluding sort space)

By sorting first, we can systematically find pairs by adjusting pointers based on whether the current sum is too small or too large, ensuring we find all possible k-sum pairs.

---
