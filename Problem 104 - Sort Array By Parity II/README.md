# 922. Sort Array By Parity II

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/sort-array-by-parity-ii/description/)

---

## Problem Description

Given an array of integers `nums`, half of the integers in `nums` are odd, and the other half are even.

Sort the array so that whenever `nums[i]` is odd, `i` is odd, and whenever `nums[i]` is even, `i` is even.

Return **any answer array** that satisfies this condition.

---

## Examples

**Example 1:**

```
Input: nums = [4,2,5,7]  
Output: [4,5,2,7]  
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
```

**Example 2:**

```
Input: nums = [2,3]  
Output: [2,3]  
```

---

## Constraints

- `2 <= nums.length <= 2 * 10⁴`  
- `nums.length` is even.  
- Half of the integers in `nums` are even.  
- `0 <= nums[i] <= 1000`

---

## Solution Strategy

To solve this problem, I used a **two-pointer in-place swap** approach with separate even/odd index trackers:

1. **Initialize** two pointers: `i = 0` (tracks even indices) and `j = 1` (tracks odd indices)
2. **Loop** while both pointers are within bounds:
   - **If `nums[i]` is even**: It's already correct at an even index — skip ahead by `i += 2`
   - **Else if `nums[j]` is odd**: It's already correct at an odd index — skip ahead by `j += 2`
   - **Else**: `nums[i]` is odd at an even index AND `nums[j]` is even at an odd index — **swap** them and advance both pointers by 2
3. **Return** `nums` — now satisfying the parity-index constraint.

### Why This Approach?

The two-pointer technique fixes misplaced elements by pairing them up for swaps:
- **Time Complexity:** O(n) — Each pointer traverses at most half the array, and each element is visited at most once
- **Space Complexity:** O(1) — All swaps are done in-place, no auxiliary array needed

The key insight is that a misplaced odd number at an even index and a misplaced even number at an odd index always come in pairs (since the counts are balanced). By independently scanning even and odd indices, we find these mismatched pairs and resolve them with a single swap. This is a natural extension of Problem 103 (Sort Array By Parity), adding the index-parity constraint.

---
