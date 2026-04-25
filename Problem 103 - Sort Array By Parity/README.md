# 905. Sort Array By Parity

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/sort-array-by-parity/description/)

---

## Problem Description

Given an integer array `nums`, move all the even integers at the beginning of the array followed by all the odd integers.

Return **any array** that satisfies this condition.

---

## Examples

**Example 1:**

```
Input: nums = [3,1,2,4]  
Output: [2,4,3,1]  
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
```

**Example 2:**

```
Input: nums = [0]  
Output: [0]  
```

---

## Constraints

- `1 <= nums.length <= 5000`  
- `0 <= nums[i] <= 5000`

---

## Solution Strategy

To solve this problem, I used a **two-pointer in-place swap** approach:

1. **Initialize** two pointers: `left = 0` and `right = len(nums) - 1`
2. **Loop** while `left < right`:
   - **Swap condition**: If `nums[left]` is odd and `nums[right]` is even (`nums[left] % 2 > nums[right] % 2`), swap them
   - **Advance `left`**: If `nums[left]` is even, it's already in the correct position — move `left` forward
   - **Advance `right`**: If `nums[right]` is odd, it's already in the correct position — move `right` backward
3. **Return** `nums` — now partitioned with all evens before odds.

### Why This Approach?

The two-pointer technique partitions the array in-place without needing extra storage:
- **Time Complexity:** O(n) — Each element is visited at most once by each pointer
- **Space Complexity:** O(1) — All swaps are done in-place, no auxiliary array needed

The comparison `nums[left] % 2 > nums[right] % 2` is a clean trick — it evaluates to `True` only when the left element is odd (remainder 1) and the right element is even (remainder 0), which is exactly when a swap is needed. The pointers converge from both ends, ensuring evens accumulate on the left and odds on the right.

---
