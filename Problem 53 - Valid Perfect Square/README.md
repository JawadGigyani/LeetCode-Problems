# 367. Valid Perfect Square

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/valid-perfect-square/description/)

---

## Problem Description

Given a positive integer `num`, return `true` if `num` is a perfect square or `false` otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must **not** use any built-in library function, such as `sqrt`.

---

## Examples

**Example 1:**

```
Input: num = 16  
Output: true  
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
```

**Example 2:**

```
Input: num = 14  
Output: false  
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
```

---

## Constraints

- `1 <= num <= 2^31 - 1`

---

## Solution Strategy

To solve this problem, I used a **binary search** approach:

1. **Edge case**: If `num < 2`, return `True` (0 and 1 are perfect squares)
2. **Initialize search range**: `left = 2`, `right = num // 2`
3. **Binary search while `left <= right`**:
   - Calculate `mid` and compute `sq = mid * mid`
   - If `sq == num`, return `True` (found the perfect square root)
   - If `sq < num`, move `left = mid + 1`
   - If `sq > num`, move `right = mid - 1`
4. If the loop ends without finding a match, return `False`.

### Why This Approach?

Binary search efficiently narrows down the candidate square root:
- **Time Complexity:** O(log n) - We halve the search space each iteration
- **Space Complexity:** O(1) - Only using a few variables

Similar to Sqrt(x) (Problem 39), but instead of finding the floor, we check for an exact match. If `mid * mid` ever equals `num`, it's a perfect square — otherwise it's not.

---
