# 69. Sqrt(x)

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/sqrtx/description/)

---

## Problem Description

Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The returned integer should be non-negative as well.

You must **not** use any built-in exponent function or operator (e.g., `pow(x, 0.5)` or `x ** 0.5`).

---

## Examples

**Example 1:**

```
Input: x = 4  
Output: 2  
Explanation: The square root of 4 is 2, so we return 2.
```

**Example 2:**

```
Input: x = 8  
Output: 2  
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
```

---

## Constraints

- `0 <= x <= 2^31 - 1`

---

## Solution Strategy

To solve this problem, I used a **binary search** approach:

1. **Handle edge case**: If `x < 2`, return `x` directly (sqrt of 0 is 0, sqrt of 1 is 1)
2. **Initialize search range**: `left = 1`, `right = x // 2` (sqrt is always ≤ x/2 for x ≥ 2)
3. **Binary search while `left <= right`**:
   - Calculate `mid` and compute `res = mid * mid`
   - If `res <= x`, the answer could be `mid` or higher → move `left = mid + 1`
   - If `res > x`, `mid` is too large → move `right = mid - 1`
4. **Return** `right` — after the loop, `right` holds the largest integer whose square is ≤ x.

### Why This Approach?

Binary search efficiently narrows down the integer square root:
- **Time Complexity:** O(log n) - We halve the search space each iteration
- **Space Complexity:** O(1) - Only using a few variables

The key insight is that when the loop ends, `right` is the floor of the square root because `left` has crossed over `right`, meaning `right * right <= x` while `(right + 1) * (right + 1) > x`.

---
