# 2011. Final Value of Variable After Performing Operations

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/)

---

## Problem Description

There is a programming language with only four operations and one variable `X`:

- `++X` and `X++` increments the value of the variable `X` by `1`.
- `--X` and `X--` decrements the value of the variable `X` by `1`.

Initially, the value of `X` is `0`.

Given an array of strings `operations` containing a list of operations, return the **final value** of `X` after performing all the operations.

---

## Examples

**Example 1:**

```
Input: operations = ["--X","X++","X++"]  
Output: 1  
Explanation: The operations are performed as follows:
Initially, X = 0.
--X: X is decremented by 1, X =  0 - 1 = -1.
X++: X is incremented by 1, X = -1 + 1 =  0.
X++: X is incremented by 1, X =  0 + 1 =  1.
```

**Example 2:**

```
Input: operations = ["++X","++X","X++"]  
Output: 3  
Explanation: The operations are performed as follows:
Initially, X = 0.
++X: X is incremented by 1, X = 0 + 1 = 1.
++X: X is incremented by 1, X = 1 + 1 = 2.
X++: X is incremented by 1, X = 2 + 1 = 3.
```

**Example 3:**

```
Input: operations = ["X++","++X","--X","X--"]  
Output: 0  
Explanation: The operations are performed as follows:
Initially, X = 0.
X++: X is incremented by 1, X = 0 + 1 = 1.
++X: X is incremented by 1, X = 1 + 1 = 2.
--X: X is decremented by 1, X = 2 - 1 = 1.
X--: X is decremented by 1, X = 1 - 1 = 0.
```

---

## Constraints

- `1 <= operations.length <= 100`  
- `operations[i]` will be either `"++X"`, `"X++"`, `"--X"`, or `"X--"`.

---

## Solution Strategy

To solve this problem, I used a **simple iteration with conditional check** approach:

1. **Initialize** `x = 0`
2. **Iterate** through each operation string `i`:
   - If `i` is `'--X'` or `'X--'`, decrement `x` by `1`
   - Otherwise (it must be `'++X'` or `'X++'`), increment `x` by `1`
3. **Return** `x`.

### Why This Approach?

Since pre/post increment and decrement behave identically for the final result, we only need to check whether the operation contains `--` or `++`:
- **Time Complexity:** O(n) — One pass through the operations array
- **Space Complexity:** O(1) — Only a single variable `x` is used

The distinction between prefix (`++X`) and postfix (`X++`) doesn't matter here since we only care about the final value, not intermediate expression results.

---
