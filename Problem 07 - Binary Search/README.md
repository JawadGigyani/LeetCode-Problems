# 704. Binary Search

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/binary-search/)

---

## Problem Description

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with **O(log n)** runtime complexity.

---

## Examples

**Example 1:**

```
Input: nums = [-1,0,3,5,9,12], target = 9  
Output: 4  
Explanation: 9 exists in nums and its index is 4
```

**Example 2:**

```
Input: nums = [-1,0,3,5,9,12], target = 2  
Output: -1  
Explanation: 2 does not exist in nums so return -1
```

---

## Constraints

- `1 <= nums.length <= 10^4`  
- `-10^4 < nums[i], target < 10^4`  
- All the integers in `nums` are unique.  
- `nums` is sorted in ascending order.

---

## Solution Strategy

To solve this problem, I used the classic **binary search** algorithm:

1. **Initialize two pointers**:
   - `l` (low) pointing to the start of the array (index 0)
   - `h` (high) pointing to the end of the array (index `len(nums) - 1`)
2. **Loop while `l <= h`**:
   - Calculate the middle index: `m = (l + h) // 2`
   - If `nums[m] == target`, we found it → return `m`
   - If `target > nums[m]`, the target is in the right half → move `l = m + 1`
   - If `target < nums[m]`, the target is in the left half → move `h = m - 1`
3. If the loop ends without finding the target, return `-1`.

### Why This Approach?

Binary search is the optimal algorithm for searching in a sorted array:
- **Time Complexity:** O(log n) - We halve the search space with each iteration
- **Space Complexity:** O(1) - We only use a few pointer variables

By repeatedly dividing the search interval in half, we can find the target (or determine it doesn't exist) in logarithmic time, which is much faster than a linear search O(n) for large arrays.

---
