# 88. Merge Sorted Array

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/merge-sorted-array/description/)

---

## Problem Description

You are given two integer arrays `nums1` and `nums2`, sorted in **non-decreasing order**, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in **non-decreasing order**.

The final sorted array should not be returned by the function, but instead be **stored inside the array `nums1`**. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.

---

## Examples

**Example 1:**

```
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3  
Output: [1,2,2,3,5,6]  
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
```

**Example 2:**

```
Input: nums1 = [1], m = 1, nums2 = [], n = 0  
Output: [1]  
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
```

**Example 3:**

```
Input: nums1 = [0], m = 0, nums2 = [1], n = 1  
Output: [1]  
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure
the merge result can fit in nums1.
```

---

## Constraints

- `nums1.length == m + n`  
- `nums2.length == n`  
- `0 <= m, n <= 200`  
- `1 <= m + n <= 200`  
- `-10⁹ <= nums1[i], nums2[j] <= 10⁹`

---

## Solution Strategy

To solve this problem, I used a **three-pointer merge from the back** approach:

1. **Initialize Three Pointers**:
   - `i = m - 1` — points to the last real element in `nums1`
   - `j = n - 1` — points to the last element in `nums2`
   - `k = m + n - 1` — points to the last position in `nums1` (the fill position)
2. **Merge from Right to Left**: While `j >= 0` (there are still elements in `nums2` to place):
   - If `i >= 0` and `nums1[i] > nums2[j]`, place `nums1[i]` at position `k` and decrement `i`
   - Otherwise, place `nums2[j]` at position `k` and decrement `j`
   - Decrement `k` after each placement
3. **Done**: The loop naturally stops when all `nums2` elements are placed. Any remaining `nums1` elements are already in their correct positions.

### Why This Approach?

Merging from the back avoids overwriting `nums1` elements that haven't been processed yet:
- **Time Complexity:** O(m + n) — Each element from both arrays is placed exactly once
- **Space Complexity:** O(1) — The merge is done entirely in-place within `nums1`

The key insight is that the trailing zeros in `nums1` provide free space at the end. By filling from the largest values backward, we never risk overwriting an unprocessed element. The loop only needs to track `j >= 0` because once all `nums2` elements are placed, the remaining `nums1` elements are already sorted in their correct positions.

---
