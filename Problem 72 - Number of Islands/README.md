# 200. Number of Islands

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/number-of-islands/description/)

---

## Problem Description

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

---

## Examples

**Example 1:**

```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1  
Explanation: All the '1's are connected, forming a single island.
```

**Example 2:**

```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3  
Explanation: There are three separate groups of connected '1's, forming three islands.
```

---

## Constraints

- `m == grid.length`  
- `n == grid[i].length`  
- `1 <= m, n <= 300`  
- `grid[i][j]` is `'0'` or `'1'`.

---

## Solution Strategy

To solve this problem, I used a **DFS flood-fill** approach:

1. **Initialize** a `visited` matrix of the same dimensions as the grid and a `count` variable
2. **Iterate** through every cell in the grid:
   - If the cell is `'1'` and not yet visited, it's the start of a new island — increment `count` and trigger a DFS
3. **Define a recursive `dfs(r, c)`**:
   - **Boundary check**: If out of bounds, on water (`'0'`), or already visited, return
   - **Mark** the cell as visited
   - **Recurse** in all four directions (up, down, left, right)
4. **Return** `count` after scanning the entire grid.

### Why This Approach?

DFS flood-fill is the classic technique for counting connected components in a grid:
- **Time Complexity:** O(m × n) — Each cell is visited at most once
- **Space Complexity:** O(m × n) — The visited matrix, plus O(m × n) recursion stack in the worst case

Each time we encounter an unvisited land cell, we've found a new island. The DFS then marks all connected land cells as visited, ensuring each island is counted exactly once.

---
