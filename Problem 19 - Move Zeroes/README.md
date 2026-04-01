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

- `1 <= nums.length <= 10⁴`  
- `-2³¹ <= nums[i] <= 2³¹ - 1`

---

## Solution Strategy (Delete-and-Append)

To solve this problem, I first used a **two-pointer with delete-and-append** approach:

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
- **Time Complexity:** O(n²) — Each `del` operation shifts elements, repeated for each zero
- **Space Complexity:** O(1) — We modify the array in-place without extra space

The right pointer `r` acts as a boundary to prevent re-processing the zeroes we've already moved to the end, ensuring the loop terminates correctly.

---

## Improved Solution (Swap-Based Two Pointer)

I later revisited this problem with a cleaner **swap-based** approach:

1. **Initialize** a write pointer `pos = 0` (tracks where the next non-zero element should go)
2. **Iterate** through the array with index `i`:
   - If `nums[i] != 0`:
     - **Swap** `nums[i]` with `nums[pos]`
     - Increment `pos` by 1
3. The array is modified **in-place** — all non-zero elements are packed to the front, and zeroes naturally end up at the back.

### Why This Improvement?

The original solution's `del` and `append` operations each cost O(n) due to element shifting, making it O(n²) overall. The swap-based approach avoids any shifting entirely:
- **Time Complexity:** O(n) — Single pass through the array, each swap is O(1)
- **Space Complexity:** O(1) — In-place with only one extra variable

The `pos` pointer always stays at or behind `i`, so every swap either places a non-zero element into its correct position or swaps an element with itself (a no-op). This guarantees that relative order is preserved without any unnecessary data movement.

---
