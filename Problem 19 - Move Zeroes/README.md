# 283. Move Zeroes

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/move-zeroes/description/)

---

## Problem Description

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this **in-place** without making a copy of the array.

---

## Examples

**Example 1:**

```
Input: nums = [0,1,0,3,12]  
Output: [1,3,12,0,0]
```

**Example 2:**

```
Input: nums = [0]  
Output: [0]
```

---

## Constraints

- `1 <= nums.length <= 10^4`  
- `-2^31 <= nums[i] <= 2^31 - 1`

---

## Solution Strategy

To solve this problem, I used a **two-pointer with delete-and-append** approach:

1. **Initialize two pointers**: `l = 0` (left) and `r = len(nums) - 1` (right boundary)
2. **Loop while `l < r`**:
   - If `nums[l] == 0`:
     - **Delete** the zero from its current position (`del nums[l]`)
     - **Append** a zero at the end (`nums.append(0)`)
     - Decrease `r` by 1 (one less non-zero element to check)
   - If `nums[l] != 0`:
     - Move `l` forward (`l += 1`)
3. The array is modified **in-place** as required.

### Why This Approach?

This approach directly moves zeroes to the end while preserving order:
- **Time Complexity:** O(n²) - Each `del` operation shifts elements, repeated for each zero
- **Space Complexity:** O(1) - We modify the array in-place without extra space

The right pointer `r` acts as a boundary to prevent re-processing the zeroes we've already moved to the end, ensuring the loop terminates correctly.

---
