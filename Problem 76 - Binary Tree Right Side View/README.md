# 199. Binary Tree Right Side View

**Difficulty:** Medium  
[LeetCode Link](https://leetcode.com/problems/binary-tree-right-side-view/description/)

---

## Problem Description

Given the `root` of a binary tree, imagine yourself standing on the **right side** of it, return the values of the nodes you can see ordered from top to bottom.

---

## Examples

**Example 1:**

![Right Side View Example 1](https://assets.leetcode.com/uploads/2024/11/24/tmpd5jn43fs-1.png)

```
Input: root = [1,2,3,null,5,null,4]  
Output: [1,3,4]  
```

**Example 2:**

![Right Side View Example 2](https://assets.leetcode.com/uploads/2024/11/24/tmpkpe40xeh-1.png)

```
Input: root = [1,2,3,4,null,null,null,5]  
Output: [1,3,4,5]  
```

**Example 3:**

```
Input: root = [1,null,3]  
Output: [1,3]  
```

**Example 4:**

```
Input: root = []  
Output: []  
```

---

## Constraints

- The number of nodes in the tree is in the range `[0, 100]`.  
- `-100 <= Node.val <= 100`

---

## Solution Strategy

To solve this problem, I used a **BFS level-order traversal** approach:

1. **Edge case**: If `root` is `None`, return an empty list
2. **Initialize** a `deque` with the root node and an empty `result` list
3. **Process level by level**: While the queue is not empty:
   - Collect all node values at the current level into a temporary list `temp`
   - For each node, enqueue its left and right children
   - **Append `temp[-1]`** (the last/rightmost value in the level) to `result`
4. **Return** `result`.

### Why This Approach?

BFS processes nodes level by level, and the last node processed at each level is the rightmost one visible from the right side:
- **Time Complexity:** O(n) — Each node is visited exactly once
- **Space Complexity:** O(w) — Where w is the maximum width of the tree

By collecting each level's values into `temp` and taking `temp[-1]`, we naturally capture the right side view. This mirrors the approach used in Problem 73 (Find Largest Value in Each Tree Row), but instead of taking the max, we take the last element.

---
