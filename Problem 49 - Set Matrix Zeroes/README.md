# 73. Set Matrix Zeroes

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/set-matrix-zeroes/description/)

---

## Problem Description

Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s.

You must do it **in place**.

---

## Examples

**Example 1:**

![Set Matrix Zeroes Example 1](https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg)

```
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]  
Output: [[1,0,1],[0,0,0],[1,0,1]]
```

**Example 2:**

![Set Matrix Zeroes Example 2](https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg)

```
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]  
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

---

## Constraints

- `m == matrix.length`  
- `n == matrix[0].length`  
- `1 <= m, n <= 200`  
- `-2^31 <= matrix[i][j] <= 2^31 - 1`

---

## Solution Strategy

To solve this problem, I used a **two-pass with tracking arrays** approach:

1. **Initialize** two tracking arrays: `track_rows` and `track_cols` (filled with 0s)
2. **First pass** — find all zeroes:
   - Iterate through the matrix
   - If `matrix[i][j] == 0`, mark `track_rows[i] = 1` and `track_cols[j] = 1`
3. **Second pass** — apply zeroes:
   - Iterate through the matrix again
   - If `track_rows[i]` or `track_cols[j]` is marked, set `matrix[i][j] = 0`

### Why This Approach?

Separating detection from modification avoids corrupting the original data:
- **Time Complexity:** O(m × n) - Two full passes through the matrix
- **Space Complexity:** O(m + n) - Tracking arrays for rows and columns

The first pass records which rows and columns need to be zeroed without modifying the matrix, preventing false positives. The second pass then applies all the changes at once.

---
