# 35. Search Insert Position

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/search-insert-position/description/)

---

## Problem Description

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with **O(log n)** runtime complexity.

---

## Examples

**Example 1:**

```
Input: nums = [1,3,5,6], target = 5  
Output: 2
```

**Example 2:**

```
Input: nums = [1,3,5,6], target = 2  
Output: 1
```

**Example 3:**

```
Input: nums = [1,3,5,6], target = 7  
Output: 4
```

---

## Constraints

- `1 <= nums.length <= 10^4`  
- `-10^4 <= nums[i] <= 10^4`  
- `nums` contains distinct values sorted in ascending order.  
- `-10^4 <= target <= 10^4`

---

## Solution Strategy

To solve this problem, I used a **binary search** approach:

1. **Initialize two pointers**:
   - `low` starting at 0
   - `high` starting at `len(nums) - 1`
2. **Loop while `low <= high`**:
   - Calculate the middle index: `mid = (low + high) // 2`
   - Get the value at mid: `guess = nums[mid]`
   - If `guess < target`, search right half → `low = mid + 1`
   - If `guess > target`, search left half → `high = mid - 1`
   - If `guess == target`, found it → return `mid`
3. **If not found**, return `low` - this is the correct insertion position.

### Why This Approach?

Binary search efficiently finds the target or its insertion point:
- **Time Complexity:** O(log n) - We halve the search space each iteration
- **Space Complexity:** O(1) - Only using a few pointer variables

The key insight is that when the loop exits without finding the target, `low` points to exactly where the target should be inserted to maintain sorted order. This is because `low` always moves past elements smaller than the target.

---
