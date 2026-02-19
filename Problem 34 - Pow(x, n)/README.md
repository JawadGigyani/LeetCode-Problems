# 50. Pow(x, n)

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/powx-n/description/)

---

## Problem Description

Implement `pow(x, n)`, which calculates `x` raised to the power `n` (i.e., x<sup>n</sup>).

---

## Examples

**Example 1:**

```
Input: x = 2.00000, n = 10  
Output: 1024.00000
```

**Example 2:**

```
Input: x = 2.10000, n = 3  
Output: 9.26100
```

**Example 3:**

```
Input: x = 2.00000, n = -2  
Output: 0.25000  
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
```

---

## Constraints

- `-100.0 < x < 100.0`  
- `-2^31 <= n <= 2^31 - 1`  
- `n` is an integer.  
- Either `x` is not zero or `n > 0`.  
- `-10^4 <= x^n <= 10^4`

---

## Solution Strategy

To solve this problem, I used a **recursive fast exponentiation (binary exponentiation)** approach:

1. **Base case**: If `n == 0`, return `1`
2. **Handle negative exponent**: If `n < 0`, convert to `x = 1/x` and `n = -n`
3. **Recursively compute half**: `half = myPow(x, n // 2)`
4. **Combine**:
   - If `n` is even: return `half * half`
   - If `n` is odd: return `x * half * half`

### Why This Approach?

Binary exponentiation reduces the number of multiplications exponentially:
- **Time Complexity:** O(log n) - We halve the exponent at each recursive step
- **Space Complexity:** O(log n) - Recursion stack depth

Instead of multiplying `x` n times (O(n)), we exploit the property that x<sup>n</sup> = (x<sup>n/2</sup>)<sup>2</sup>. This halves the problem at each step, achieving logarithmic time complexity.

---
