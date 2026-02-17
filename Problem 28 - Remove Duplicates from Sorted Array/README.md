# 26. Remove Duplicates from Sorted Array

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)

---

## Problem Description

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates **in-place** such that each unique element appears only once. The relative order of the elements should be kept the same.

Return the number of unique elements `k`. The first `k` elements of `nums` should contain the unique numbers in sorted order.

---

## Examples

**Example 1:**

```
Input: nums = [1,1,2]  
Output: 2, nums = [1,2,_]  
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
```

**Example 2:**

```
Input: nums = [0,0,1,1,1,2,2,3,3,4]  
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]  
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
```

---

## Constraints

- `1 <= nums.length <= 3 * 10^4`  
- `-100 <= nums[i] <= 100`  
- `nums` is sorted in non-decreasing order.

---

## Solution Strategy

To solve this problem, I used a **two-pointer** approach:

1. **Initialize** `left = 1` (the position to place the next unique element)
2. **Iterate** `right` from index 1 through the array:
   - If `nums[right] != nums[right - 1]`, we found a new unique element:
     - Place it at position `left`: `nums[left] = nums[right]`
     - Increment `left`
3. **Return** `left` — the count of unique elements.

### Why This Approach?

The two-pointer technique efficiently removes duplicates in-place:
- **Time Complexity:** O(n) - We traverse the array once
- **Space Complexity:** O(1) - We modify the array in-place

Since the array is sorted, duplicates are always adjacent. The `left` pointer marks where the next unique value should go, while `right` scans ahead to find it. Elements before `left` form the deduplicated result.

---
