# 226. Invert Binary Tree

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/invert-binary-tree/description/)

---

## Problem Description

Given the `root` of a binary tree, invert the tree, and return its root.

---

## Examples

**Example 1:**

![Invert Binary Tree Example 1](https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg)

```
Input: root = [4,2,7,1,3,6,9]  
Output: [4,7,2,9,6,3,1]
```

**Example 2:**

![Invert Binary Tree Example 2](https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg)

```
Input: root = [2,1,3]  
Output: [2,3,1]
```

**Example 3:**

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

To solve this problem, I used a **recursive swap** approach:

1. **Base case**: If `root` is `None`, return `None`
2. **Swap** the left and right children: `root.left, root.right = root.right, root.left`
3. **Recurse** on both subtrees: `invertTree(root.left)` and `invertTree(root.right)`
4. **Return** `root`.

### Why This Approach?

Recursive swapping mirrors the tree at every level:
- **Time Complexity:** O(n) - We visit every node exactly once
- **Space Complexity:** O(h) - Recursion stack depth, where h is the tree height

The Pythonic tuple swap makes the inversion clean and readable. By swapping first and then recursing, each subtree gets fully inverted from top to bottom.

---
