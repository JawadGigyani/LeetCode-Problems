# 2652. Sum Multiples

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/sum-multiples/description/)

---

## Problem Description

Given a positive integer `n`, find the sum of all integers in the range `[1, n]` inclusive that are divisible by `3`, `5`, or `7`.

Return an integer denoting the sum of all numbers in the given range satisfying the constraint.

---

## Examples

**Example 1:**

```
Input: n = 7  
Output: 21  
Explanation: Numbers in the range [1, 7] that are divisible by 3, 5, or 7 are 3, 5, 6, 7. The sum of these numbers is 21.
```

**Example 2:**

```
Input: n = 10  
Output: 40  
Explanation: Numbers in the range [1, 10] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9, 10. The sum of these numbers is 40.
```

**Example 3:**

```
Input: n = 9  
Output: 30  
Explanation: Numbers in the range [1, 9] that are divisible by 3, 5, or 7 are 3, 5, 6, 7, 9. The sum of these numbers is 30.
```

---

## Constraints

- `1 <= n <= 10^3`

---

## Solution Strategy

To solve this problem, I used a **simple iteration with modulo check** approach:

1. **Initialize** `total_sum = 0`
2. **Iterate** through every number `i` from `1` to `n`:
   - If `i % 3 == 0` or `i % 5 == 0` or `i % 7 == 0`, add `i` to `total_sum`
3. **Return** `total_sum`.

### Why This Approach?

A straightforward linear scan is efficient given the small constraint:
- **Time Complexity:** O(n) - We check every number in the range
- **Space Complexity:** O(1) - Only using a single accumulator variable

The modulo operator cleanly checks divisibility, and using `or` ensures a number is only added once even if it's divisible by multiple values (e.g., 15 is divisible by both 3 and 5).

---
