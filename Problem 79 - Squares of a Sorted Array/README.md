# 977. Squares of a Sorted Array

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/squares-of-a-sorted-array/description/)

---

## Problem Description

Given an integer array `nums` sorted in **non-decreasing order**, return an array of the squares of each number sorted in non-decreasing order.

---

## Examples

**Example 1:**

```
Input: nums = [-4,-1,0,3,10]  
Output: [0,1,9,16,100]  
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
```

**Example 2:**

```
Input: nums = [-7,-3,2,3,11]  
Output: [4,9,9,49,121]  
```

---

## Constraints

- `1 <= nums.length <= 10⁴`  
- `-10⁴ <= nums[i] <= 10⁴`  
- `nums` is sorted in non-decreasing order.

---

## Solution Strategy

To solve this problem, I used a **square-in-place then sort** approach:

1. **Square each element**: Iterate through the array and replace each element with its square (`nums[num] *= nums[num]`)
2. **Sort** the squared array
3. **Return** the sorted result.

### Why This Approach?

Squaring can disrupt the original order because negative numbers become positive (e.g., `(-4)² = 16 > 3² = 9`), so a re-sort is needed:
- **Time Complexity:** O(n log n) — Dominated by the sorting step
- **Space Complexity:** O(1) — Squaring is done in-place (excluding sort's internal space)

A simple and clean solution. An O(n) two-pointer approach is also possible by comparing absolute values from both ends, but the sort-based method is concise and well within the problem's constraints.

---
