# 485. Max Consecutive Ones

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/max-consecutive-ones/description/)

---

## Problem Description

Given a binary array `nums`, return the maximum number of consecutive `1`'s in the array.

---

## Examples

**Example 1:**

```
Input: nums = [1,1,0,1,1,1]  
Output: 3  
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
```

**Example 2:**

```
Input: nums = [1,0,1,1,0,1]  
Output: 2
```

---

## Constraints

- `1 <= nums.length <= 10^5`  
- `nums[i]` is either `0` or `1`.

---

## Solution Strategy

To solve this problem, I used a **linear scan with counter** approach:

1. **Initialize** `count = 0` (current streak) and `max_ones = 0` (best streak)
2. **Iterate through the array**:
   - If `nums[i] == 1`, increment `count`
   - If `nums[i] == 0`, reset `count` to 0
   - Update `max_ones` with the maximum of `max_ones` and `count`
3. **Return** `max_ones`.

### Why This Approach?

A single pass with a running counter is the most straightforward solution:
- **Time Complexity:** O(n) - We traverse the array once
- **Space Complexity:** O(1) - Only using two variables

The counter grows during streaks of 1s and resets on any 0. By tracking the maximum at every step, we capture the longest consecutive run.

---
