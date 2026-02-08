# 33. Search in Rotated Sorted Array

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)

---

## Problem Description

There is an integer array `nums` sorted in ascending order (with distinct values).

Prior to being passed to your function, `nums` is possibly left rotated at an unknown index `k` such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]`.

For example, `[0,1,2,4,5,6,7]` might be left rotated by 3 indices and become `[4,5,6,7,0,1,2]`.

Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with **O(log n)** runtime complexity.

---

## Examples

**Example 1:**

```
Input: nums = [4,5,6,7,0,1,2], target = 0  
Output: 4
```

**Example 2:**

```
Input: nums = [4,5,6,7,0,1,2], target = 3  
Output: -1
```

**Example 3:**

```
Input: nums = [1], target = 0  
Output: -1
```

---

## Constraints

- `1 <= nums.length <= 5000`  
- `-10^4 <= nums[i] <= 10^4`  
- All values of `nums` are unique.  
- `nums` is an ascending array that is possibly rotated.  
- `-10^4 <= target <= 10^4`

---

## Solution Strategy

To solve this problem, I used a **modified binary search** that handles the rotation:

1. **Initialize two pointers**: `low = 0` and `high = len(nums) - 1`
2. **Loop while `low <= high`**:
   - Calculate `mid = (low + high) // 2`
   - If `nums[mid] == target`, return `mid`
   - **Determine which half is sorted**:
     - If `nums[low] <= nums[mid]`, the **left half is sorted**:
       - If target is in range `[nums[low], nums[mid])`, search left → `high = mid - 1`
       - Otherwise, search right → `low = mid + 1`
     - Else, the **right half is sorted**:
       - If target is in range `(nums[mid], nums[high]]`, search right → `low = mid + 1`
       - Otherwise, search left → `high = mid - 1`
3. If not found, return `-1`.

### Why This Approach?

The key insight is that in a rotated sorted array, **at least one half is always sorted**:
- **Time Complexity:** O(log n) - Binary search with constant-time decisions
- **Space Complexity:** O(1) - Only using pointer variables

By identifying which half is sorted, we can determine if the target lies within that sorted range and eliminate half the search space each iteration.

---
