# 543. Diameter of Binary Tree

**Difficulty:** Easy  
[LeetCode Link](https://leetcode.com/problems/diameter-of-binary-tree/description/)

---

## Problem Description

Given the `root` of a binary tree, return the length of the **diameter** of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of **edges** between them.

---

## Examples

**Example 1:**

![Diameter of Binary Tree](https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg)

```
Input: root = [1,2,3,4,5]  
Output: 3  
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
```

**Example 2:**

```
Input: root = [1,2]  
Output: 1
```

---

## Constraints

- The number of nodes in the tree is in the range `[1, 10^4]`.  
- `-100 <= Node.val <= 100`

---

## Solution Strategy

To solve this problem, I used a **recursive DFS (height calculation)** approach:

1. **Initialize** `self.max_diameter = 0` to track the longest path
2. **Define a recursive `height(node)` function**:
   - Base case: if `node is None`, return `0`
   - Recursively compute `left_height` and `right_height`
   - Update `max_diameter` with `left_height + right_height` (the path through this node)
   - Return `1 + max(left_height, right_height)` (height of current subtree)
3. **Call** `height(root)` and **return** `self.max_diameter`.

### Why This Approach?

Computing height while tracking diameter avoids redundant traversals:
- **Time Complexity:** O(n) - We visit every node exactly once
- **Space Complexity:** O(h) - Recursion stack depth, where h is the tree height

The key insight is that the diameter passing through any node equals the sum of its left and right subtree heights. By checking this at every node during height computation, we find the global maximum in a single traversal.

---
