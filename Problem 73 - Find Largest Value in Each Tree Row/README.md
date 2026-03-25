# 515. Find Largest Value in Each Tree Row

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/)

---

## Problem Description

Given the `root` of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

---

## Examples

**Example 1:**

![Find Largest Value Example 1](https://assets.leetcode.com/uploads/2020/08/21/largest_e1.jpg)

```
Input: root = [1,3,2,5,3,null,9]  
Output: [1,3,9]  
Explanation:
Row 0: max(1) = 1
Row 1: max(3, 2) = 3
Row 2: max(5, 3, 9) = 9
```

**Example 2:**

```
Input: root = [1,2,3]  
Output: [1,3]  
Explanation:
Row 0: max(1) = 1
Row 1: max(2, 3) = 3
```

---

## Constraints

- The number of nodes in the tree will be in the range `[0, 10⁴]`.  
- `-2³¹ <= Node.val <= 2³¹ - 1`

---

## Solution Strategy

To solve this problem, I used a **BFS level-order traversal** approach:

1. **Edge case**: If `root` is `None`, return an empty list
2. **Initialize** a `deque` with the root node and an empty `result` list
3. **Process level by level**: While the queue is not empty:
   - Record the current queue `length` (number of nodes at this level)
   - Initialize `highest` to negative infinity
   - **Iterate** through all nodes at this level — for each node, update `highest` with `max(node.val, highest)` and enqueue its children
   - **Append** `highest` to `result`
4. **Return** `result`.

### Why This Approach?

BFS naturally processes the tree level by level, making it ideal for row-based queries:
- **Time Complexity:** O(n) — Each node is visited exactly once
- **Space Complexity:** O(w) — Where w is the maximum width of the tree (largest number of nodes at any level)

By tracking the queue length at each iteration, we process exactly one row per outer loop. The `max` comparison within each row finds the largest value without needing extra storage.

---
