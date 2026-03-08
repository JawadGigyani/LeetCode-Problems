# 101. Symmetric Tree

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/symmetric-tree/description/)

---

## Problem Description

Given the `root` of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

---

## Examples

**Example 1:**

![Symmetric Tree Example 1](https://assets.leetcode.com/uploads/2021/02/19/symtree1.jpg)

```
Input: root = [1,2,2,3,4,4,3]  
Output: true
```

**Example 2:**

![Symmetric Tree Example 2](https://assets.leetcode.com/uploads/2021/02/19/symtree2.jpg)

```
Input: root = [1,2,2,null,3,null,3]  
Output: false
```

---

## Constraints

- The number of nodes in the tree is in the range `[1, 1000]`.  
- `-100 <= Node.val <= 100`

---

## Solution Strategy

To solve this problem, I used a **recursive mirror comparison** approach:

1. **Define a helper `isMirror(left_root, right_root)`**:
   - If both are `None`, return `True` (symmetric)
   - If only one is `None`, return `False` (not symmetric)
   - Return whether values are equal **and** the outer pair is mirrored **and** the inner pair is mirrored:
     - `left_root.val == right_root.val`
     - `isMirror(left_root.left, right_root.right)` (outer)
     - `isMirror(left_root.right, right_root.left)` (inner)
2. **Start** with `isMirror(root.left, root.right)`.

### Why This Approach?

Recursive mirror checking elegantly compares opposite subtrees:
- **Time Complexity:** O(n) - We visit every node once
- **Space Complexity:** O(h) - Recursion stack depth, where h is the tree height

The key insight is comparing **cross-pairs**: left's left with right's right (outer), and left's right with right's left (inner). This ensures the tree is a mirror image at every level.

---
