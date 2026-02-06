# 1929. Concatenation of Array

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/concatenation-of-array/description/)

---

## Problem Description

Given an integer array `nums` of length `n`, you want to create an array `ans` of length `2n` where `ans[i] == nums[i]` and `ans[i + n] == nums[i]` for `0 <= i < n` (0-indexed).

Specifically, `ans` is the concatenation of two `nums` arrays.

Return the array `ans`.

---

## Examples

**Example 1:**

```
Input: nums = [1,2,1]  
Output: [1,2,1,1,2,1]  
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
```

**Example 2:**

```
Input: nums = [1,3,2,1]  
Output: [1,3,2,1,1,3,2,1]  
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
```

---

## Constraints

- `n == nums.length`  
- `1 <= n <= 1000`  
- `1 <= nums[i] <= 1000`

---

## Solution Strategy

To solve this problem, I used Python's **list concatenation** operator:

1. **Concatenate the array with itself** using the `+` operator: `nums + nums`
2. This creates a new array containing all elements of `nums` followed by all elements of `nums` again.
3. **Return** the resulting concatenated array.

### Why This Approach?

Python's list concatenation makes this problem trivial:
- **Time Complexity:** O(n) - Creating a new list of 2n elements
- **Space Complexity:** O(n) - The result array of size 2n (required by the problem)

This one-liner solution leverages Python's expressive syntax to solve the problem in the most concise and readable way possible.

---
